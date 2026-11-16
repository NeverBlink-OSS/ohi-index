Chem-DCAT-AP https://github.com/nfdi-de/chem-dcat-ap

Release v0.1.0rc4. Package created (its files downloaded or sources' hashes created) on 2026-10-30.
The ontology file is from https://nfdi-de.github.io/chem-dcat-ap/v0.1.0rc4/schema/merged-yaml/chem_dcat_ap.yaml, the schema as one file, made upstream. It holds its own modules and DCAT-AP+ (all 51 classes and 265 slots of `nfdi/dcat-ap-plus/0.1.0rc5`), so it does not depend on that package.
The file is a remote source.

# Copyright

The repository is under the MIT License, Copyright (c) 2025 Philip Strömert. The schema itself states `license: CC-BY 4.0`. Both are listed.

# License file

`LICENSE`: Downloaded on 2026-10-22 from https://raw.githubusercontent.com/nfdi-de/chem-dcat-ap/v0.1.0rc4/LICENSE.

`legalcode.txt`: The CC BY 4.0 legal code, copied from `w3c/dcat/3`.

# Changes

The changes below are in `chem_dcat_ap.patch.yaml`, a JSON Patch applied to the file when the package is published.

- Removed the imports `dcatap_plus:latest/schema/dcat_ap_plus`, `chemical_entities_ap`, `chemical_reaction_ap`, `material_entities_ap`. The file already holds what they define, but still lists them, so it could not be loaded on its own; `dcatap_plus:latest/...` would also be fetched from the web. `linkml:types` is kept.
- Added the 12 prefixes the merged file uses or carried over from DCAT-AP+ but does not declare, copied from DCAT-AP+ v0.1.0rc5: `spdx`, `odrl`, `eli`, `locn`, `xsd`, `dcatap`, `qb`, `sh`, `vl`, `iana`, `epos`, `SOSA`.
- Added the 4 prefixes the merged file uses but lost from its modules, as `chemical_entities_ap.yaml` and `material_entities_ap.yaml` at tag `v0.1.0rc4` declare them: `AFX` (`http://purl.allotrope.org/ontologies/property#AFX_`, for `AFX:0000940`), `EDAM` (`http://edamontology.org/data_`, for `EDAM:2140`), `chemical_entities_ap` and `material_entities_ap` (in `class_uri` of three mixins).
- Removed the 19 types copied in from `linkml:types` (`string` to `sparqlpath`, marked `imported_from: linkml:types`). The file still imports `linkml:types`, so each was defined twice. The 3 DCAT-AP+ types `duration`, `hexBinary` and `nonNegativeInteger` are kept.
