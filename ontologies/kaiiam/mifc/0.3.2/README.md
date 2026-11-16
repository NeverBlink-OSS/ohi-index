mifc, by kaiiam. A minimum information standard checklist formalizing the description of food composition data and related metadata. Schema id: https://w3id.org/kaiiam/mifc

Depends on no other package.

Package created (its files downloaded or sources' hashes created) on 2026-11-04.
The schema file is from https://github.com/kaiiam/mifc/blob/v0.3.2/src/mifc/schema/mifc.yaml.
The file at the release tag `v0.3.2`.
The file is a remote source.

Notes:

- 5 classes, 80 slots, 9 enums; schema id https://w3id.org/kaiiam/mifc.
- The version is the release tag.

# Copyright

Licensed under the MIT License: https://opensource.org/licenses/MIT (as stated in the schema itself).

# Changes

The changes below are in `mifc.patch.yaml`, a JSON Patch applied to the file when the package is published.

- The 247 permissible values of `CountryCode` written in full form: `AFG: Afghanistan` becomes the value `AFG` with the description `Afghanistan`, which is how LinkML reads the short form.

- `examples` of the 6 slots `food_primary_type`, `food_primary_type_label`, `food_cooking_method`, `food_acquisition_city`, `food_acquisition_country_subdivision`, `food_distributor_city` written as a list holding their one example (`value: Tucson` and so on). `examples` takes a list.
Nothing else changed.

# License file

`LICENSE`: The LICENSE of the kaiiam/mifc repository, at the same tag as the schema, https://github.com/kaiiam/mifc/blob/v0.3.2/LICENSE. A source of the package, not kept in the folder.
