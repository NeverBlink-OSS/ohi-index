submission-schema, by microbiomedata. The NMDC submission schema. Schema id: https://example.com/nmdc_submission_schema

Depends on no other package.

Package created (its files downloaded or sources' hashes created) on 2026-11-04.
The schema file is from https://github.com/microbiomedata/submission-schema/blob/v7.6.5/src/nmdc_submission_schema/schema/nmdc_submission_schema.yaml.
The file at the release tag `v7.6.5`.
The file is a remote source.

Notes:

- 21 classes, 584 slots, 121 enums; schema id https://example.com/nmdc_submission_schema.
- The version is the release tag.

# Copyright

Licensed under the MIT License: https://opensource.org/licenses/MIT (as stated in the LICENSE of the repository at the release tag, not in the schema).

# Changes

The changes below are in `submission-schema.patch.yaml`, a JSON Patch applied to the file when the package is published.

- Added the 5 abstract slots `EMSL`, `JGI-Metagenomics`, `JGI-Metatranscriptomics`, `MIxS Inspired`, `Sample ID`. They name sections that `slot_group` points to, which must name a slot, and the file leaves them out, so those references point to nothing.
- Removed the permissible value `''`, an empty name, of `wall_texture_enum`. A permissible value needs a name.
- Removed `slot_usage: []` of the 4 classes `SampIdNewTermsMixin`, `DhInterface`, `SampleData`, `NamedThing`. `slot_usage` takes a map, and an empty list says nothing.
- Split the 3 `see_also` CURIEs that join two terms with `|` (`MIxS:experimental_factor|additional_info`, `MIxS:biomass|microbial_biomass`, `MIxS:org_nitro|tot_nitro_cont_meth`) into one CURIE per term, in 9 places (3 slots and their slot usages).
- Added the prefix `MIxS` (`https://w3id.org/mixs/`, the namespace the schema declares as `MIXS`), which the schema uses in `see_also` but does not declare. Prefixes are case-sensitive.

- Removed `domain_of` (1,159) and `owner` (1,160) from the slot usages where they name classes the schema doesn't have (`Biosample`, `FieldResearchSite`, `ProcessedSample`, `Study`, classes of `nmdc/nmdc-schema`). The LinkML loader fills both itself; upstream's file carries them over from nmdc-schema with the slot usages it copies. No slot usage named a class of the schema there.
Nothing else changed.

# License file

`LICENSE`: The LICENSE of the microbiomedata/submission-schema repository, at the same tag as the schema, https://github.com/microbiomedata/submission-schema/blob/v7.6.5/LICENSE. A source of the package, not kept in the folder.
