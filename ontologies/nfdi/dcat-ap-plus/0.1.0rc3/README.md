DCAT-AP+, by NFDI. Extension of the DCAT application profile for describing research data and the activities that produce it. Schema id: https://w3id.org/nfdi-de/dcat-ap-plus/

Depends on no other package.

Package created (its files downloaded or sources' hashes created) on 2026-10-30.
The ontology file is from https://nfdi-de.github.io/dcat-ap-plus/v0.1.0rc3/schema/merged-yaml/dcat_ap_plus.yaml.
The file is a remote source.

Notes:

- Release candidate.
- The schema states `version: 0.1.0rc2`; the version is the release's, `0.1.0rc3`.

# Copyright

Licensed under the MIT License: https://opensource.org/licenses/MIT (as stated in the LICENSE of the repository, https://github.com/nfdi-de/dcat-ap-plus, not in the file) and CC BY 4.0: https://creativecommons.org/licenses/by/4.0/ (as stated in the file itself).

# Changes

The changes below are in `dcat_ap_plus.patch.yaml`, a JSON Patch applied to the file when the package is published.

- Removed the 19 types copied in from `linkml:types` (`string` to `sparqlpath`, marked `imported_from: linkml:types`). The file still imports `linkml:types`, so each was defined twice.
- Wrote the 4 `obligation_level` values given as permissible values (`text: RECOMMENDED` with a description) as the value itself, `obligation_level: RECOMMENDED`. `obligation_level` takes a value of an enum. Later releases write it so.
- Added the prefixes of CURIEs the schema uses but does not declare: from the version in the index, `owl` (`http://www.w3.org/2002/07/owl#`, as `nfdi/dcat-ap-plus/0.1.0rc5` declares it).

Nothing else changed.

# License file

`LICENSE`: The LICENSE of the nfdi-de/dcat-ap-plus repository at the release tag `v0.1.0rc3`, https://github.com/nfdi-de/dcat-ap-plus/blob/v0.1.0rc3/LICENSE. A source of the package, not kept in the folder.

`legalcode.txt`: The plain-text legal code of the license, https://creativecommons.org/licenses/by/4.0/legalcode.txt. A source of the package, not kept in the folder.
