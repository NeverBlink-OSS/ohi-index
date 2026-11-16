Chem-DCAT-AP, by NFDI. DCAT application profile for describing chemistry research data. Schema id: https://w3id.org/nfdi-de/dcat-ap-plus/chemistry/

Depends on no other package.

Package created (its files downloaded or sources' hashes created) on 2026-10-30.
The ontology file is from https://nfdi-de.github.io/chem-dcat-ap/v0.1.0rc3/schema/merged-yaml/chem_dcat_ap.yaml.
The file is a remote source.

Notes:

- Release candidate.
- Merged upstream, holds DCAT-AP+.

# Copyright

Licensed under the MIT License: https://opensource.org/licenses/MIT (as stated in the LICENSE of the repository, https://github.com/nfdi-de/chem-dcat-ap, not in the file) and CC BY 4.0: https://creativecommons.org/licenses/by/4.0/ (as stated in the file itself).

# Changes

The changes below are in `chem_dcat_ap.patch.yaml`, a JSON Patch applied to the file when the package is published.

- Removed the imports `dcatapplus:latest/schema/dcat_ap_plus`, `chemical_entities_ap`, `chemical_reaction_ap`, `material_entities_ap`. The file is the schema merged into one file upstream and already holds what they define, but still lists them, so it could not be loaded on its own. `linkml:*` imports are kept.
- Removed the 19 types copied in from `linkml:types` (`string` to `sparqlpath`, marked `imported_from: linkml:types`). The file still imports `linkml:types`, so each was defined twice.
- Wrote the 4 `obligation_level` values given as permissible values (`text: RECOMMENDED` with a description) as the value itself, `obligation_level: RECOMMENDED`. `obligation_level` takes a value of an enum. Later releases write it so.
- Added the prefixes of CURIEs the schema uses but does not declare: from the version in the index, `AFX` (`http://purl.allotrope.org/ontologies/property#AFX_`, as `nfdi/chem-dcat-ap/0.1.0rc4` declares it), `EDAM` (`http://edamontology.org/data_`, as `nfdi/chem-dcat-ap/0.1.0rc4` declares it), `chemical_entities_ap` (`https://w3id.org/nfdi-de/dcat-ap-plus/chemistry/entity/`, as `nfdi/chem-dcat-ap/0.1.0rc4` declares it), `dcatap` (`http://data.europa.eu/r5r/`, as `nfdi/chem-dcat-ap/0.1.0rc4` declares it), `eli` (`http://data.europa.eu/eli/ontology#`, as `nfdi/chem-dcat-ap/0.1.0rc4` declares it), `epos` (`https://www.epos-eu.org/epos-dcat-ap#`, as `nfdi/chem-dcat-ap/0.1.0rc4` declares it), `iana` (`https://www.iana.org/assignments/`, as `nfdi/chem-dcat-ap/0.1.0rc4` declares it), `locn` (`http://www.w3.org/ns/locn#`, as `nfdi/chem-dcat-ap/0.1.0rc4` declares it), `material_entities_ap` (`https://w3id.org/nfdi-de/dcat-ap-plus/materials/`, as `nfdi/chem-dcat-ap/0.1.0rc4` declares it), `odrl` (`http://www.w3.org/ns/odrl/2/`, as `nfdi/chem-dcat-ap/0.1.0rc4` declares it), `spdx` (`http://spdx.org/rdf/terms#`, as `nfdi/chem-dcat-ap/0.1.0rc4` declares it), `xsd` (`http://www.w3.org/2001/XMLSchema#`, as `nfdi/chem-dcat-ap/0.1.0rc4` declares it).

Nothing else changed.

# License file

`LICENSE`: The LICENSE of the nfdi-de/chem-dcat-ap repository at the release tag `v0.1.0rc3`, https://github.com/nfdi-de/chem-dcat-ap/blob/v0.1.0rc3/LICENSE. A source of the package, not kept in the folder.

`legalcode.txt`: The plain-text legal code of the license, https://creativecommons.org/licenses/by/4.0/legalcode.txt. A source of the package, not kept in the folder.
