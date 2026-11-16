standards-schema, by bridge2ai. Data schema for Bridge2AI Standards. Schema id: https://w3id.org/bridge2ai/standards-schema

Depends on no other package.

Package created (its files downloaded or sources' hashes created) on 2026-11-02.
The schema file is from https://github.com/bridge2ai/standards-schemas/blob/be379bed6336b1f282bf036ef71d517849dfb3f9/src/standards_schemas/schema/standards_schema.yaml, the file at commit be379bed6336b1f282bf036ef71d517849dfb3f9 of the default branch (the repository has no stable release tag).
The file is a remote source.

Notes:

- 4 classes, 26 slots, 0 enums; schema id https://w3id.org/bridge2ai/standards-schema.
- Listed in the LinkML Schema Registry as `standards-schemas`, https://github.com/bridge2ai/standards-schemas.
- The version is the download date.

# Copyright

Licensed under the MIT License: https://opensource.org/licenses/MIT (as stated in the schema itself).

# Changes

The changes below are in `standards-schemas.patch.yaml`, a JSON Patch applied to the file when the package is published.

- Added the prefix `MESH` (`http://id.nlm.nih.gov/mesh/`, the namespace the schema declares as `mesh`). The slot `subclass_of` lists `MESH:isa` in `exact_mappings` (as Biolink Model does), and prefixes are case-sensitive, so the schema does not declare the prefix of that CURIE. `MESH:isa` names no MeSH descriptor; it is kept as written.

Nothing else changed.

# License file

`LICENSE`: The LICENSE of the bridge2ai/standards-schemas repository, at the same commit as the schema, https://github.com/bridge2ai/standards-schemas/blob/be379bed6336b1f282bf036ef71d517849dfb3f9/LICENSE. A source of the package, not kept in the folder.
