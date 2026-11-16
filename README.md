# ohi index

This is the ontology package index for ohi, the ontology package manager.

Browse and download published ontologies on [ohi.dev](https://ohi.dev/). To learn how to use the CLI or SDKs, see the [ohi documentation](https://ohi.dev/docs/).

## Layout

Each ontology release has its own folder at `ontologies/<namespace>/<name>/<version>/`.

The folder contains a package manifest (`ohi-package.yaml`) and a README. Ontology and license files can be stored in the folder or referenced by URL in the manifest.

A package follows the naming convention `namespace/name@version`.  For example, `acme/widgets@1.0.0` lives in `ontologies/acme/widgets/1.0.0/`.

## Contributing

To request an ontology, [open an issue](https://github.com/NeverBlink-OSS/ohi-index/issues/new?template=ontology-request.yml) with its official source, the version you need if known, and what you want to use it for. You do not need to prepare a package.

To submit a new ontology or a new version yourself:

1. Fork this repository and create a branch.
2. Add a folder `ontologies/<namespace>/<name>/<version>/` with:
    - `ohi-package.yaml`, which describes the package (see the example below),
    - the ontology file, or a `sources` entry pointing to it upstream,
    - the full license text and any required copyright notices,
    - a short `README.md` identifying the original sources and any changes you made.
3. Open a pull request against `main` for maintainer review.

The ontology's license must allow redistribution. If you are not an author or publisher of the ontology, add yourself or your organization under `maintainers` so there is someone to contact about the index entry.

Follow the [Code of Conduct](CODE_OF_CONDUCT.md) when participating.

## Creating a Manifest (ohi-package.yaml)

Consider an example manifest for `acme/widgets@1.0.0`:

```yaml
namespace: acme
name: widgets
version: "1.0.0"
language: owl                # owl | rdfs | linkml | ossie
syntax: turtle               # turtle | rdfxml | ntriples | jsonld | yaml
roots: [widgets.ttl]
licenses: ["CC-BY-4.0"]
licenseFiles: [LICENSE]
dependencies: []
title: "ACME Widgets Ontology"
description: "Terms for describing widgets, their parts and suppliers."
keywords: ["widgets", "manufacturing", "supply chain"]
authors:
  - name: "Jane Doe"
publishers:
  - name: "ACME Ontology Group"
    link: "https://ontology.acme.example/"
maintainers:
  - name: "Alex Smith"
    contact: "alex@example.com"
    link: "https://github.com/alex-smith-example"
originalSources: ["https://ontology.acme.example/widgets"]
```

- Match `namespace`, `name` and `version` to the folder path
- List exactly one ontology entry file in `roots`.
- Use [SPDX license identifiers](https://spdx.org/licenses/) where available.
- Use `licenseFiles` for paths to full license texts and `copyrightFiles` for paths to separate copyright notices.

If the ontology imports other ontologies, list their exact releases under `dependencies`, for example `dependencies: ["acme/core@2.3.0"]`. These releases must already be published on ohi.

To use an upstream file instead of storing it here, add a `sources` entry. Replace the example URL, SHA-256 and byte count with values for the exact file you are submitting:

```yaml
sources:
  - url: https://ontology.acme.example/widgets/1.0.0/widgets.ttl
    name: widgets.ttl
    sha256: "<64 lowercase hex characters>"
    size: 123456
```

## Questions and issues

For index related questions or problems, [open an issue here](https://github.com/NeverBlink-OSS/ohi-index/issues). For any inquiry on the ohi sdk, api or website, use [NeverBlink-OSS/ohi](https://github.com/NeverBlink-OSS/ohi).

## Licensing

Project-owned material is licensed under [Apache-2.0](LICENSE).

Ontologies retain their own licenses, recorded in each `ohi-package.yaml` and its referenced `licenseFiles`.
