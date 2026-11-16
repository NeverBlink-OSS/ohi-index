submission-schema, by microbiomedata. The NMDC submission schema. Schema id: https://example.com/nmdc_submission_schema

Depends on no other package.

Package created (its files downloaded or sources' hashes created) on 2026-11-04.
The schema file is from https://github.com/microbiomedata/submission-schema/blob/v1.0.0/src/nmdc_submission_schema/schema/nmdc_submission_schema.yaml.
The file at the release tag `v1.0.0`.
The file is a remote source.

Notes:

- 21 classes, 589 slots, 119 enums; schema id https://example.com/nmdc_submission_schema.
- The version is the release tag.

# Copyright

Licensed under the MIT License: https://opensource.org/licenses/MIT (as stated in the LICENSE of the repository at the release tag, not in the schema).

# Changes

The changes below are in `submission-schema.patch.yaml`, a JSON Patch applied to the file when the package is published.

- Removed the permissible value `''`, an empty name, of `wall_texture_enum`. A permissible value needs a name.
- The file writes the removed value as an explicit key (`? ''`); the patched file, written out as YAML again, has no such key.

- Removed `domain_of` (1,080) and `owner` (1,080) from the slot usages where they name classes the schema doesn't have (`Biosample`, `Study`, classes of `nmdc/nmdc-schema`). The LinkML loader fills both itself; upstream's file carries them over from nmdc-schema with the slot usages it copies. No slot usage named a class of the schema there.
Nothing else changed.

# License file

`LICENSE`: The LICENSE of the microbiomedata/submission-schema repository, at the same tag as the schema, https://github.com/microbiomedata/submission-schema/blob/v1.0.0/LICENSE. A source of the package, not kept in the folder.
