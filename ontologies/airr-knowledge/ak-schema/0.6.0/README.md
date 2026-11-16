ak-schema, by airr-knowledge. AIRR Knowledge Schema. Schema id: https://github.com/airr-knowledge/ak-schema

Depends on no other package.

Package created (its files downloaded or sources' hashes created) on 2026-11-04.
The schema file is from https://github.com/airr-knowledge/ak-schema/blob/v0.6.0/project/linkml/ak_schema.yaml.
The file at the release tag `v0.6.0`.
The file is a remote source.

Notes:

- The file is upstream's merged schema: `project/linkml/ak_schema.yaml`, which the repository generates from `src/ak_schema/schema/ak_top.yaml` and its modules, with `linkml:types` written in and no imports. Until 2026-11-09 the package held the module `src/ak_schema/schema/ak_airr.yaml` alone, which names the class `AIRRStandards` of another module, so it can't be read on its own.
- 114 classes, 495 slots, 61 enums; schema id https://github.com/airr-knowledge/ak-schema.
- The version is the release tag.

# Copyright

Licensed under the GNU General Public License 3.0, version 3 only: https://www.gnu.org/licenses/gpl-3.0.html (as stated in the LICENSE of the repository at the release tag; the schema states `GNU GPL v3.0`). No notice says "or any later version", so by section 14 of the GPL only version 3 applies (SPDX `GPL-3.0-only`).

# Changes

The changes below are in `ak-schema.patch.yaml`, a JSON Patch applied to the file when the package is published.

- Permissible values `+` and `-` of `StrandEnum` renamed to `plus_sign` and `hyphen_minus` (their `text` too), each with the original as an alias.

Nothing else changed.

# License file

`LICENSE`: The LICENSE of the airr-knowledge/ak-schema repository, at the same tag as the schema, https://github.com/airr-knowledge/ak-schema/blob/v0.6.0/LICENSE. A source of the package, not kept in the folder.
