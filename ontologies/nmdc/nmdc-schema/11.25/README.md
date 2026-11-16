National Microbiome Data Collaborative Schema https://github.com/microbiomedata/nmdc-schema

Release 11.25. Package created (its files downloaded or sources' hashes created) on 2026-10-30.
The ontology file is from https://github.com/microbiomedata/nmdc-schema/blob/v11.25/nmdc_schema/nmdc_materialized_patterns.yaml, the file at the release tag `v11.25`. It is the schema as one file, made upstream: its local imports merged and its structured patterns filled in. It states `version: 0.0.0`; the PyPI release of the same file, `nmdc_schema/nmdc_materialized_patterns.yaml` in https://files.pythonhosted.org/packages/b2/09/80e87345935789f7fac896854114f15899610b482e7b0b83132a7c7b800f/nmdc_schema-11.25-py3-none-any.whl, fills in `11.25`. A file inside a wheel cannot be a package source, so the release tag's file is the source and the version is set by the patch.
The file is a remote source.

# Copyright

The NMDC Schema is licensed under Creative Commons Zero v1.0 Universal.

# License file

`LICENSE`: Downloaded on 2026-10-22 from https://raw.githubusercontent.com/microbiomedata/nmdc-schema/v11.25/LICENSE.

# Changes

The changes below are in `nmdc_materialized_patterns.patch.yaml`, a JSON Patch applied to the file when the package is published.

The fixes of the earlier merged copy of this schema (2026-10-06) that are still needed, and three more:

- Set `version` to `11.25`, as the PyPI release does. The file at the tag states `0.0.0`.
- Renamed the permissible value `%` of `UnitEnum` to `PERCENT`, with `%` as an alias.
- Added the prefix `OM` (`http://www.ontology-of-units-of-measure.org/resource/om-2/`) for `OM:degreeCelsius`.
- Added the prefix `CO_715` (`https://cropontology.org/rdf/CO_715:`) for the example term `CO_715:0000189` of `growth_facil`. It is the Crop Ontology's own RDF address for its terms; the Bioregistry has no entry for `CO_715`.
- Added the 3 abstract slots `JGI-Metagenomics`, `MIxS Inspired` and `Sample ID`, copied from the earlier merged copy. They name the sections of the NMDC submission portal, and 19 slots point to them in `slot_group`, which must name a slot. The materialized file leaves them out, so those references point to nothing.

The `orcid:` CURIEs need no change any more: the schema now declares `orcid`.
