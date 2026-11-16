synbio-schema, by iarpa-felix. A schema for synthetic biology, inspired by IARPA FELIX. Schema id: http://www.semanticweb.org/mam/ontologies/2022/7/synbio

Depends on no other package.

Package created (its files downloaded or sources' hashes created) on 2026-11-02.
The schema file is from https://github.com/iarpa-felix/synbio-schema/blob/v0.0.1/src/synbio_schema/schema/synbio_schema.yaml, the file at the release tag `v0.0.1`.
The file is a remote source.

Notes:

- 7 classes, 65 slots, 9 enums; schema id http://www.semanticweb.org/mam/ontologies/2022/7/synbio.
- Listed in the LinkML Schema Registry as `synbio-schema`, https://github.com/iarpa-felix/synbio-schema.

# Copyright

Licensed under the MIT License: https://opensource.org/licenses/MIT (as stated in the LICENSE of the repository, not in the schema).

# Changes

The changes below are in `synbio-schema.patch.yaml`, a JSON Patch applied to the file when the package is published.

- Added the prefix `IDO` (`http://purl.obolibrary.org/obo/IDO_`, the OBO namespace of the Infectious Disease Ontology, as in the `obo_context` CURIE map), which the schema uses in `IDO:0000581`, an exact mapping of the permissible value `antibiotic resistance`, but does not declare. The namespace is picked by hand: the schema names no CURIE map.

Nothing else changed.

# License file

`LICENSE`: The LICENSE of the iarpa-felix/synbio-schema repository, at the same tag as the schema, https://github.com/iarpa-felix/synbio-schema/blob/v0.0.1/LICENSE. A source of the package, not kept in the folder.
