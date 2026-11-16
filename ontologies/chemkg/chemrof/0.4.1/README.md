Chemical Entities Mixtures and Reactions Ontological Framework, by chemkg. Schema for chemistry ontology classes. Schema id: https://w3id.org/chemrof

Depends on no other package.

Package created (its files downloaded or sources' hashes created) on 2026-11-02.
The schema file is from https://github.com/chemkg/chemrof/blob/v0.4.1/src/chemrof/schema/chemrof.yaml, the file at the release tag `v0.4.1`.
The file is a remote source.

Notes:

- 134 classes, 242 slots, 14 enums; schema id https://w3id.org/chemrof.
- Listed in the LinkML Schema Registry as `chemrof`, https://github.com/chemkg/chemrof.

# Copyright

Licensed under CC0 1.0: https://creativecommons.org/publicdomain/zero/1.0/ (as stated in the schema itself).

# Changes

The changes below are in `chemrof.patch.yaml`, a JSON Patch applied to the file when the package is published.

- `deprecated: true` of the class `IsomeraseReaction` and the slot `has_physiologically_stable_form` written as the text `'true'`. `deprecated` takes a text (why the element is deprecated).
- The permissible values `acid: CHEBI:39141` and `base: CHEBI:39142` of `BronstedAcidBaseRoleEnum` written in full form: `acid` with the description `CHEBI:39141`, which is how LinkML reads the short form, though the CURIEs look meant as the meaning.
- Added the prefix `OntoRXN` (`http://www.semanticweb.com/OntoRxn#`, the namespace the schema declares as `OntoRxn`), used in `OntoRXN:hasInChi`. Prefixes are case-sensitive.
- Added the prefix `edam` (`http://edamontology.org/`, EDAM's own namespace, as in the Bioregistry), used in `edam:data_0846`. The schema lists `idot_context`, which has only `EDAM`, with an identifiers.org namespace. The namespace is picked by hand.

- In `union_of` of the class `ChemicalEntityOrGrouping`, `chemical entity grouping class` replaced with `ChemicalGroupingClass`. No class has that name or title; the nearest is `ChemicalGroupingClass` (title `chemical grouping class`), picked by hand.
Nothing else changed.

# License file

`LICENSE`: The LICENSE of the chemkg/chemrof repository, at the same tag as the schema, https://github.com/chemkg/chemrof/blob/v0.4.1/LICENSE. A source of the package, not kept in the folder.
