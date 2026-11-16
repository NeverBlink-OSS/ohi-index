NMDC Schema, by National Microbiome Data Collaborative. National Microbiome Data Collaborative schema for microbiome samples, studies and analyses. Schema id: https://w3id.org/nmdc/nmdc

Depends on no other package.

Package created (its files downloaded or sources' hashes created) on 2026-10-30.
The ontology file is from https://github.com/microbiomedata/nmdc-schema/blob/v11.24.1/nmdc_schema/nmdc_materialized_patterns.yaml.
The file is the one at the release tag `v11.24.1`.
The file is a remote source.

Notes:

- The schema states `version: 0.0.0`; the version is the release's, `11.24.1`.

# Copyright

Licensed under CC0 1.0: https://creativecommons.org/publicdomain/zero/1.0/ (as stated in the LICENSE of the repository, https://github.com/microbiomedata/nmdc-schema, not in the file).

# Changes

The changes below are in `nmdc_materialized_patterns.patch.yaml`, a JSON Patch applied to the file when the package is published.

- Renamed the permissible value `%` of `UnitEnum` to `PERCENT`, with `%` as an alias.
- Added the 3 abstract slots `JGI-Metagenomics`, `MIxS Inspired`, `Sample ID`. They name sections that `slot_group` points to, which must name a slot, and the file leaves them out, so those references point to nothing.
- Added the prefixes of CURIEs the schema uses but does not declare: from the version in the index, `CO_715` (`https://cropontology.org/rdf/CO_715:`, as `nmdc/nmdc-schema/11.25` declares it), `OM` (`http://www.ontology-of-units-of-measure.org/resource/om-2/`, as `nmdc/nmdc-schema/11.25` declares it).

Nothing else changed.

# License file

`LICENSE`: The LICENSE of the microbiomedata/nmdc-schema repository at the release tag `v11.24.1`, https://github.com/microbiomedata/nmdc-schema/blob/v11.24.1/LICENSE. A source of the package, not kept in the folder.
