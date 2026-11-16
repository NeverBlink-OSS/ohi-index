The Ontology Metadata Schema of the TIB Terminology Service, by StroemPhi. A schema for ontology metadata (WIP). Schema id: http://terminology.tib.eu/schema

Depends on no other package.

Package created (its files downloaded or sources' hashes created) on 2026-11-02.
The schema file is from https://github.com/StroemPhi/Ontology-Metadata/blob/1f6b3d7355be2bbf1bbec0207601ee634650cd6e/src/ontology_metadata/schema/ontology_metadata.yaml, the file at commit 1f6b3d7355be2bbf1bbec0207601ee634650cd6e of the default branch (the repository has no stable release tag).
The file is a remote source.

Notes:

- 5 classes, 50 slots, 0 enums; schema id http://terminology.tib.eu/schema.
- Listed in the LinkML Schema Registry as `Ontology-Metadata`, https://github.com/StroemPhi/Ontology-Metadata.
- The version is the schema's `version`.

# Copyright

Licensed under the GNU General Public License 3.0, version 3 only: https://www.gnu.org/licenses/gpl-3.0.html (as stated in the LICENSE of the repository, not in the schema). No notice says "or any later version", so by section 14 of the GPL only version 3 applies (SPDX `GPL-3.0-only`).

# Changes

The changes below are in `ontology-metadata.patch.yaml`, a JSON Patch applied to the file when the package is published.

- Added the prefixes `dcterm` (`http://purl.org/dc/terms/`, the namespace the schema declares as `dcterms`), `vann` (`http://purl.org/vocab/vann/`), `doap` (`http://usefulinc.com/ns/doap#`) and `mod` (`https://w3id.org/mod#`), which the schema uses in `slot_uri` and mappings but does not declare. The namespaces of `vann`, `doap` and `mod` are picked by hand, each its vocabulary's own.
- The patched file is written out as YAML again, which also rewrites the file's last line, the slot `appliedMethodology:` with no value and no line break after it.

Nothing else changed.

# License file

`LICENSE`: The LICENSE of the StroemPhi/Ontology-Metadata repository, at the same commit as the schema, https://github.com/StroemPhi/Ontology-Metadata/blob/1f6b3d7355be2bbf1bbec0207601ee634650cd6e/LICENSE. A source of the package, not kept in the folder.
