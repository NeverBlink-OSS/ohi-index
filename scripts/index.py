#!/usr/bin/env python3
"""Sends folders of the index to the ohi hub, for the GitHub workflows.

    index.py --ref REF [--dry-run] FOLDER...
    index.py --ref REF [--dry-run] --changed BASE [--head HEAD]
        Asks the hub to publish the folders under ontologies/, given as
        namespace/name/version, or the ones changed between BASE and HEAD
        (default: the checked-out commit). --head lets a pull request's commits
        be diffed without checking them out, so none of their code runs.
        --changed leaves out the folders on hold in ontologies/skip.tsv.
        The hub reads everything from GitHub at REF.
        Without --dry-run, only starts the jobs and prints their ids.
        With --dry-run, the hub writes nothing; waits for every job, prints
        its result and fails if one fails.
        When the hub's queue is full (429), a folder is tried again every two
        seconds until the hub takes it.
        HUB_URL is the hub. With HUB_PASSWORD set, sends it as basic auth,
        user HUB_USER (default: ohi-index).

The hub decides what a valid package is.
"""

from __future__ import annotations

import argparse
import base64
import http.client
import json
import os
import subprocess
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ONTOLOGIES = ROOT / "ontologies"
SKIP = ONTOLOGIES / "skip.tsv"

DONE = {"completed", "failed", "cancelled"}
# Seconds to wait before each new try of a GET that got no answer
RETRIES = [5, 10, 20, 40, 60]


def ontology_folders() -> list[str]:
    """The version folders, as namespace/name/version."""
    return sorted(
        p.relative_to(ONTOLOGIES).as_posix()
        for p in ONTOLOGIES.glob("*/*/*")
        if p.is_dir() and not any(part.startswith(".") for part in p.relative_to(ONTOLOGIES).parts)
    )


def git(*args: str) -> list[str]:
    return subprocess.run(["git", *args], cwd=ROOT, check=True, capture_output=True, text=True).stdout.splitlines()


def folders_at(commit: str) -> set[str]:
    """The version folders at a commit, as namespace/name/version, read from git, not the working tree."""
    return {
        "/".join(parts[1:])
        for name in git("ls-tree", "-r", "-d", "--name-only", commit, "--", "ontologies/")
        if len(parts := name.split("/")) == 4 and not any(part.startswith(".") for part in parts)
    }


def changed_folders(base: str, head: str) -> list[str]:
    """Ontology folders with changes between base and head that still exist at head, less those on hold."""
    if set(base) == {"0"}:
        # A push that created the branch has no before, so take everything.
        folders = ontology_folders()
    else:
        names = git("diff", "--name-only", f"{base}...{head}", "--", "ontologies/")
        changed = {"/".join(name.split("/")[1:4]) for name in names if name.count("/") >= 4}
        folders = sorted(changed & folders_at(head))
    lines = SKIP.read_text(encoding="utf-8").splitlines()[1:] if SKIP.is_file() else []
    held = {line.partition("\t")[0].strip() for line in lines if line.strip()}
    for folder in folders:
        if folder in held:
            print(f"{folder}: on hold in {SKIP.name}, skipped", file=sys.stderr)
    return [folder for folder in folders if folder not in held]


def request(method: str, url: str, body: dict | None = None) -> tuple[int, str]:
    data = json.dumps(body).encode() if body is not None else None
    req = urllib.request.Request(url, data=data, method=method)
    if data is not None:
        req.add_header("Content-Type", "application/json")
    if password := os.environ.get("HUB_PASSWORD"):
        user = os.environ.get("HUB_USER") or "ohi-index"
        req.add_header("Authorization", "Basic " + base64.b64encode(f"{user}:{password}".encode()).decode())
    # A POST is not tried again: it may have reached the hub and started a job.
    waits = RETRIES if method == "GET" else []
    for attempt in range(len(waits) + 1):
        try:
            with urllib.request.urlopen(req, timeout=60) as response:
                return response.status, response.read().decode("utf-8", "replace")
        except urllib.error.HTTPError as e:
            return e.code, e.read().decode("utf-8", "replace")
        except (OSError, http.client.HTTPException) as e:
            # No answer at all, such as a dropped connection or a timeout
            if attempt == len(waits):
                raise
            path = urllib.parse.urlsplit(url).path
            print(f"{method} {path}: {e!r}, trying again in {waits[attempt]}s", file=sys.stderr, flush=True)
            time.sleep(waits[attempt])


def hub_error(error: dict | str) -> str:
    """A hub error as one line: its message and fields, such as the requestId and jobId
    the hub's log has the full error under. Any other answer, such as the gateway's, as it is.
    """
    if isinstance(error, str):
        try:
            parsed = json.loads(error)
        except ValueError:
            return error
        if not isinstance(parsed, dict) or "message" not in parsed:
            return error
        error = parsed
    fields = ", ".join(f"{key} {value}" for key, value in (error.get("fields") or {}).items())
    return f"{error.get('message')} ({fields})" if fields else str(error.get("message"))


def start(hub: str, body: dict) -> str | None:
    """Starts a hub job: its id, or None if the hub refused."""
    folder = body["folder"]
    queue_full = False
    while (answer := request("POST", f"{hub}/publish/", body))[0] == 429:
        if not queue_full:
            print(f"{folder}: hub queue full, waiting for room: {hub_error(answer[1])}", file=sys.stderr)
        queue_full = True
        time.sleep(2)
    status, text = answer
    if status != 202:
        print(f"{folder}: refused ({status}): {hub_error(text)}", file=sys.stderr)
        return None
    job = json.loads(text)["id"]
    print(f"{folder}: job {job}", flush=True)
    return job


def finish(hub: str, folder: str, job: str) -> bool:
    """Waits for a hub job and prints its result: whether it completed."""
    while True:
        status, text = request("GET", f"{hub}/publish/{job}")
        if status != 200:
            print(f"{folder}: could not read job {job} ({status}): {text}", file=sys.stderr)
            return False
        state = json.loads(text)
        if state.get("status") in DONE:
            break
        time.sleep(5)
    if state["status"] != "completed":
        error = state.get("error")
        print(f"{folder}: {state['status']}: {hub_error(error) if error else 'no error given'}", file=sys.stderr)
        return False
    status, text = request("GET", f"{hub}/publish/{job}/result")
    print(f"{folder}: {text}" if status == 200 else f"{folder}: completed, no result ({status})", flush=True)
    return True


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("folders", nargs="*", help="folders under ontologies/, as namespace/name/version")
    parser.add_argument("--changed", metavar="BASE", help="the folders changed between BASE and HEAD instead")
    parser.add_argument("--head", default="HEAD", help="the commit --changed compares with BASE (default: HEAD)")
    parser.add_argument("--ref", required=True, help="commit sha or branch the hub reads")
    parser.add_argument("--hub", default=os.environ.get("HUB_URL"), help="hub URL (default: $HUB_URL)")
    parser.add_argument("--dry-run", action="store_true", help="write nothing, wait for every job")
    args = parser.parse_args()
    if bool(args.folders) == bool(args.changed):
        parser.error("takes either folders or --changed")
    if not args.hub:
        parser.error("needs --hub or HUB_URL")

    folders = changed_folders(args.changed, args.head) if args.changed else [f.strip("/") for f in args.folders]
    if not folders:
        print("nothing to publish")
        return 0
    hub = args.hub.rstrip("/")
    body = {"ref": args.ref, "dryRun": True} if args.dry_run else {"ref": args.ref}
    jobs = {folder: start(hub, {**body, "folder": folder}) for folder in folders}
    failed = [folder for folder, job in jobs.items() if job is None]
    if args.dry_run:
        failed += [folder for folder, job in jobs.items() if job is not None and not finish(hub, folder, job)]
    if failed:
        print(f"failed: {' '.join(failed)}", file=sys.stderr)
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
