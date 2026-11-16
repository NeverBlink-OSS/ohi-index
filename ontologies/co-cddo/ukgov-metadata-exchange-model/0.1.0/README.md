UK Government Organisations, by co-cddo. A metadata model for describing data assets for exchanging between UK government organisations. Schema id: https://www.gov.uk/api/organisations

Depends on no other package.

Package created (its files downloaded or sources' hashes created) on 2026-11-02.
The schema file is from https://github.com/co-cddo/ukgov-metadata-exchange-model/blob/v0.1.0/src/model/uk-gov-orgs.yaml, the file at the release tag `v0.1.0`.
The file is a remote source.

Notes:

- 0 classes, 0 slots, 1 enums; schema id https://www.gov.uk/api/organisations.
- Listed in the LinkML Schema Registry as `ukgov-metadata-exchange-model`, https://github.com/co-cddo/ukgov-metadata-exchange-model.

# Copyright

Licensed under the Open Government Licence 3.0: https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/ (as stated in the schema itself).

# Changes

The changes below are in `ukgov-metadata-exchange-model.patch.yaml`, a JSON Patch applied to the file when the package is published.

- `extensions` of the 1,176 permissible values of `OrganisationValues` written as a map by tag instead of a list of `tag`/`value` maps. No tag occurs twice in a list, so nothing is lost.
- Import `linkml:types` added. The schema sets `default_range: string` but neither defines nor imports the types.

Nothing else changed.

# License file

`LICENSE`: The plain-text legal code of the license, https://raw.githubusercontent.com/spdx/license-list-data/v3.29.0/text/OGL-UK-3.0.txt. A source of the package, not kept in the folder.
