essdive-sample-reporting-format, by heycatwonton. ESS-DIVE recommends registering samples for Global Sample Numbers (IGSNs) through the System for Earth Sample Registration (SESAR). Schema id: https://w3id.org/ess-dive-community/essdive-sample-reporting-format

Depends on no other package.

Package created (its files downloaded or sources' hashes created) on 2026-11-02.
The schema file is from https://github.com/heycatwonton/EssDiveSampleRF/blob/3cf80f046ccc74cf9d3a01325691c4b83ec074c1/src/essdivesamplerf/schema/essdivesamplerf.yaml, the file at commit 3cf80f046ccc74cf9d3a01325691c4b83ec074c1 of the default branch (the repository has no stable release tag).
The file is a remote source.

Notes:

- 3 classes, 45 slots, 6 enums; schema id https://w3id.org/ess-dive-community/essdive-sample-reporting-format.
- Listed in the LinkML Schema Registry as `EssDiveSampleRF`, https://github.com/heycatwonton/EssDiveSampleRF.
- The version is the download date.

# Copyright

Licensed under the MIT License: https://opensource.org/licenses/MIT (as stated in the LICENSE of the repository, not in the schema).

# Changes

The changes below are in `essdivesamplerf.patch.yaml`, a JSON Patch applied to the file when the package is published.

- Added the 6 abstract slots `Environmental Context`, `Location`, `Sample Access`, `Sample Collection Details`, `Sample Description`, `Sample IDs and Related Identifiers`. They name sections that `slot_group` points to, which must name a slot, and the file leaves them out, so those references point to nothing.

Nothing else changed.

# License file

`LICENSE`: The LICENSE of the heycatwonton/EssDiveSampleRF repository, at the same commit as the schema, https://github.com/heycatwonton/EssDiveSampleRF/blob/3cf80f046ccc74cf9d3a01325691c4b83ec074c1/LICENSE. A source of the package, not kept in the folder.
