NMDC Schema, by National Microbiome Data Collaborative. National Microbiome Data Collaborative schema for microbiome samples, studies and analyses. Schema id: https://w3id.org/nmdc/nmdc

Depends on no other package.

Package created (its files downloaded or sources' hashes created) on 2026-10-30.
The ontology file is from https://github.com/microbiomedata/nmdc-schema/blob/v10.1.1/nmdc_schema/nmdc_materialized_patterns.yaml.
The file is the one at the release tag `v10.1.1`.
The file is a remote source.

Notes:

- The schema states `version: 0.0.0`; the version is the release's, `10.1.1`.

# Copyright

Licensed under CC0 1.0: https://creativecommons.org/publicdomain/zero/1.0/ (as stated in the LICENSE of the repository, https://github.com/microbiomedata/nmdc-schema, not in the file).

# Changes

The changes below are in `nmdc_materialized_patterns.patch.yaml`, a JSON Patch applied to the file when the package is published.

- Added the 5 abstract slots `EMSL`, `JGI-Metagenomics`, `JGI-Metatranscriptomics`, `MIxS Inspired`, `Sample ID`. They name sections that `slot_group` points to, which must name a slot, and the file leaves them out, so those references point to nothing.
- Removed the permissible value `''`, an empty name, of `wall_texture_enum`. A permissible value needs a name.
- Added the prefixes of CURIEs the schema uses but does not declare: from the version in the index, `MIxS` (`https://w3id.org/mixs/`, as `nmdc/nmdc-schema/11.25` declares `MIXS`).

Nothing else changed.

# License file

`LICENSE`: The LICENSE of the microbiomedata/nmdc-schema repository at the release tag `v10.1.1`, https://github.com/microbiomedata/nmdc-schema/blob/v10.1.1/LICENSE. A source of the package, not kept in the folder.
