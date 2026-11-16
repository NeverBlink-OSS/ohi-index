information-resource-registry, by biolink. The information resource registry is a listing of data sources present in the NCATS Data Translator system. Schema id: https://w3id.org/biolink/information_resource_registry.yaml

Depends on no other package.

Package created (its files downloaded or sources' hashes created) on 2026-11-04.
The schema file is from https://github.com/biolink/information-resource-registry/blob/v1.0.0/src/information_resource_registry/schema/information_resource_registry.yaml.
The file at the release tag `v1.0.0`.
The file is a remote source.

Notes:

- 2 classes, 9 slots, 3 enums; schema id https://w3id.org/biolink/information_resource_registry.yaml.
- The version is the release tag.

# Copyright

Licensed under CC0 1.0: https://creativecommons.org/publicdomain/zero/1.0/ (as stated in the schema itself).

# Changes

The changes below are in `information-resource-registry.patch.yaml`, a JSON Patch applied to the file when the package is published.

- Added the prefixes `oboInOwl` (`http://www.geneontology.org/formats/oboInOwl#`), `SO` (`http://purl.obolibrary.org/obo/SO_`) and `BIOGRID` (`http://identifiers.org/biogrid/`), which `emit_prefixes` names but the schema does not declare. The namespaces come from the maps the schema lists there, in its order: `oboInOwl` from `semweb_context`, `SO` from `obo_context` (`idot_context` has `http://identifiers.org/so/`), `BIOGRID` from `idot_context` (`monarch_context` has `http://thebiogrid.org/`).

Nothing else changed.

# License file

`legalcode.txt`: The plain-text legal code of the license, https://creativecommons.org/publicdomain/zero/1.0/legalcode.txt. A source of the package, not kept in the folder.
