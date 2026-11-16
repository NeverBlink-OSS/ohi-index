# ohi index

The package index for [ohi.dev](https://ohi.dev/), the ontology package manager.

Each folder in the index is one release of an ontology. Once a change is merged to `main`, the new packages become available on [ohi.dev](https://ohi.dev/) and through the ohi client.

The ohi source code is at [github.com/NeverBlink-OSS/ohi](https://github.com/NeverBlink-OSS/ohi).

## Layout

Each package version lives in `ontologies/<namespace>/<name>/<version>/`, with its `ohi-package.yaml`, the ontology file (or a link to it), the license texts and a README.

A package is named `namespace/name@version`, for example `acme/widgets@1.0.0`.

## Contributing

New ontologies and new versions are added through pull requests.

1. Fork this repository and create a branch.
2. Add a folder `ontologies/<namespace>/<name>/<version>/` with:
   - `ohi-package.yaml`, which describes the package (see below),
   - the ontology file, or a `sources` entry pointing to it upstream,
   - the full license text,
   - a short `README.md` saying where the files come from and what, if anything, was changed.
3. Open a pull request. A maintainer reviews it and starts the automated checks.
4. Once merged, the package is available on [ohi.dev](https://ohi.dev/).

Generally:

- **The ontology needs a license** that allows it to be shared.
- **Third parties must add a maintainer.** If you are not an author or publisher of the ontology, add yourself (or your organization) under `maintainers`, so there is someone to contact about the package in the index.

### `ohi-package.yaml`

```yaml
namespace: acme
name: widgets
version: "1.0.0"             # always quoted, must match the folder name
language: owl                # owl | rdfs | linkml | ossie
syntax: turtle               # turtle | rdfxml | ntriples | jsonld | yaml
roots: [widgets.ttl]         # the ontology entry file, exactly one
licenses: ["CC-BY-4.0"]      # SPDX identifiers where they exist
licenseFiles: [LICENSE]
dependencies: ["acme/core@2.3.0"]
title: "ACME Widgets Ontology"
description: "Terms for describing widgets, their parts and suppliers."
keywords: ["widgets", "manufacturing", "supply chain"]
authors:
  - name: "Jane Doe"
publishers:
  - name: "ACME Ontology Group"
    link: "https://ontology.acme.example/"
maintainers:                 # required when you are not an author or publisher
  - name: "Alex Smith"
    contact: "alex@example.com"
    link: "https://github.com/alex-smith-example"
originalSources: ["https://ontology.acme.example/widgets"]
```

To use a file from upstream instead of storing it here, list it under `sources`:

```yaml
roots: [widgets.ttl]
sources:
  - url: https://ontology.acme.example/widgets/1.0.0/widgets.ttl
    sha256: "<64 lowercase hex characters>"
    size: 123456              # bytes
```

## Questions and issues

If you have any question or a problem, open an issue here. For the ohi client or site, use [NeverBlink-OSS/ohi](https://github.com/NeverBlink-OSS/ohi).
