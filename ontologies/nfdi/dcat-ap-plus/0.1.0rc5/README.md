DCAT-AP+ (DCAT-AP-PLUS) https://github.com/nfdi-de/dcat-ap-plus

Release v0.1.0rc5. Package created (its files downloaded or sources' hashes created) on 2026-10-30.
The ontology file is from https://nfdi-de.github.io/dcat-ap-plus/v0.1.0rc5/schema/merged-yaml/dcat_ap_plus.yaml, the schema as one file, made upstream. It imports only `linkml:types`, so it is used as it is, apart from the changes below.
The file is a remote source.

# Copyright

The repository is under the MIT License, Copyright (c) 2025 Philip Strömert. The schema itself states `license: CC-BY 4.0`. Both are listed.

# License file

`LICENSE`: Downloaded on 2026-10-22 from https://raw.githubusercontent.com/nfdi-de/dcat-ap-plus/v0.1.0rc5/LICENSE.

`legalcode.txt`: The CC BY 4.0 legal code, copied from `w3c/dcat/3`.

# Changes

The changes below are in `dcat_ap_plus.patch.yaml`, a JSON Patch applied to the file when the package is published.

- Added the prefix `owl` (`http://www.w3.org/2002/07/owl#`), which the schema uses in `implements: owl:NamedIndividual` but does not declare.
- Removed the 19 types copied in from `linkml:types` (`string` to `sparqlpath`, marked `imported_from: linkml:types`). The file still imports `linkml:types`, so each was defined twice. The schema's own types `duration`, `hexBinary` and `nonNegativeInteger` are kept.
