namo, by monarch-initiative. NAMO (New Approach Methodology Ontology) is a comprehensive schema for representing diverse in vitro and in silico model systems used as alternatives to traditional animal testing. Schema id: https://w3id.org/monarch-initiative/namo

Depends on no other package.

Package created (its files downloaded or sources' hashes created) on 2026-11-02.
The schema file is from https://github.com/monarch-initiative/namo/blob/ec7a5fe9e322240eb10f94f5f801976ee914902c/src/namo/schema/namo.yaml, the file at commit ec7a5fe9e322240eb10f94f5f801976ee914902c of the default branch (the repository has no stable release tag).
The file is a remote source.

Notes:

- 56 classes, 4 slots, 33 enums; schema id https://w3id.org/monarch-initiative/namo.
- Listed in the LinkML Schema Registry as `namo`, https://github.com/monarch-initiative/namo.
- The version is the download date.

# Copyright

Licensed under the BSD 3-Clause License: https://opensource.org/licenses/BSD-3-Clause (as stated in the schema itself).

# Changes

The changes below are in `namo.patch.yaml`, a JSON Patch applied to the file when the package is published.

- In 7 enums and 5 `include` entries, the dynamic enum query (`source_nodes`, `is_direct`, `relationship_types`) moved from `permissible_values` to `reachable_from`, where LinkML defines it. Under `permissible_values` its keys read as permissible values named `source_nodes` and so on.

Nothing else changed.

# License file

`LICENSE`: The LICENSE of the monarch-initiative/namo repository, at the same commit as the schema, https://github.com/monarch-initiative/namo/blob/ec7a5fe9e322240eb10f94f5f801976ee914902c/LICENSE. A source of the package, not kept in the folder.
