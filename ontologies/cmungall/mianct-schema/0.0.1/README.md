Minimal Information About a new Cell Type, by cmungall. Minimal Information About a New Cell Type. Schema id: https://w3.org/mianct

Depends on no other package.

Package created (its files downloaded or sources' hashes created) on 2026-11-02.
The schema file is from https://github.com/cmungall/mianct-schema/blob/71484be062e2c1e522a6458f342134dfa7978094/model/schema/mianct.yaml, the file at commit 71484be062e2c1e522a6458f342134dfa7978094 of the default branch (the repository has no stable release tag).
The file is a remote source.

Notes:

- 2 classes, 11 slots, 3 enums; schema id https://w3.org/mianct.
- Listed in the LinkML Schema Registry as `mianct-schema`, https://github.com/cmungall/mianct-schema.
- The version is the schema's `version`.

# Copyright

Licensed under CC0 1.0: https://creativecommons.org/publicdomain/zero/1.0/ (as stated in the schema itself).

# Changes

The changes below are in `mianct-schema.patch.yaml`, a JSON Patch applied to the file when the package is published.

- Added the prefixes `BFO` (`http://purl.obolibrary.org/obo/BFO_`) and `RO` (`http://purl.obolibrary.org/obo/RO_`), which the schema uses as `slot_uri` (`BFO:0000050`, `RO:0002162`). The schema lists `obo_context` in `default_curi_maps`, which gives these namespaces.
- Added the prefix `WIKIDATA` (`http://www.wikidata.org/entity/`, Wikidata's entity namespace), used in `WIKIDATA:Q16521` and given by neither CURIE map the schema lists. The namespace is picked by hand.

Nothing else changed.

# License file

`legalcode.txt`: The plain-text legal code of the license, https://creativecommons.org/publicdomain/zero/1.0/legalcode.txt. A source of the package, not kept in the folder.
