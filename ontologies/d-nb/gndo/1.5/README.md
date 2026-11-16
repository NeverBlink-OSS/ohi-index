GND Ontology, by Deutsche Nationalbibliothek (DNB). GND stands for "Gemeinsame Normdatei" (Integrated Authority File) and offers a broad range of elements to describe authorities. Vocabulary IRI: http://d-nb.info/standards/elementset/gnd#

Depends on no other package.

Package created (its files downloaded or sources' hashes created) on 2026-11-04.
The ontology file is from https://lov.linkeddata.es/dataset/vocabs/gndo/versions/2015-10-01.n3.
That is the copy Linked Open Vocabularies (LOV) keeps of the vocabulary's version of 2015-10-01, which its link https://lov.linkeddata.es/dataset/lov/vocabs/gndo/versions/2015-10-01.n3 redirects to. No URL of the publisher serves that version without a redirect, so LOV's copy is used.
The file is stored in this folder, because it was changed, see below.

Notes:

- 58 classes, 233 properties in its own namespace, http://d-nb.info/standards/elementset/gnd#, 8 of the terms deprecated.
- The version is the one the file states.
- LOV tags: Catalogs.

# Copyright

Licensed under CC0 1.0: https://creativecommons.org/publicdomain/zero/1.0/ (as stated in the file itself).

# Changes

- Removed `gndo:dateOfEstablishment rdfs:subPropertyOf gndo:dateOfEstablishment` and `gndo:dateOfTermination rdfs:subPropertyOf gndo:dateOfTermination`, each one item of a `rdfs:subPropertyOf` list; the other items stay. Every property is a subproperty of itself, so the triple says nothing.

Nothing else changed.

# License file

`legalcode.txt`: The plain-text legal code of the license, https://creativecommons.org/publicdomain/zero/1.0/legalcode.txt. A source of the package, not kept in the folder.
