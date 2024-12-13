# Legacy

This directory contains old stuff.

## The `nmdc-documentation` directory

Most of the files in `./nmdc-documentation` are files that we copied from
[commit `8786ff5a`](https://github.com/microbiomedata/NMDC_documentation/commit/8786ff5a63be21d38e8a01cce6f4fecc073526ac)
in the [NMDC_documentation](https://github.com/microbiomedata/NMDC_documentation) repository.
That was the latest commit on the `main` branch as of August 28, 2024.

In addition to the files we copied, the directory also contains some files that are _exclusive_ to this repository;
e.g., `Dockerfile` and `.gitignore`.

### Omissions

When copying the aforementioned files from the `NMDC_documentation` repository, we _omitted_ the following files:

- Schema element documentation in `docs/reference/metadata`
- Schema-related images in `docs/_static/images/reference/metadata`
- Schema in `docs/_static/jsonschema`

Instead of maintaining a local copy of that documentation here, we redirect visitors to the _standalone_
[schema documentation](https://microbiomedata.github.io/nmdc-schema/).

> **Example:** When someone visits `/reference/metadata/xylene.html` on this documentation website,
> they'll be automatically redirected to https://microbiomedata.github.io/nmdc-schema/xylene/. This redirection
> is configured in `./nmdc-documentation/src/conf.py`.

You can compare the `./nmdc-documentation/src` directory with the corresponding directory in the
upstream repository, by issuing these commands from the root directory of this repository:

```shell
# Clone the upstream repository onto your computer.
git clone https://github.com/microbiomedata/NMDC_documentation.git /tmp/NMDC_documentation

# Use Git to compare the corresponding directories. 
git diff --stat /tmp/NMDC_documentation/docs ./legacy/nmdc-documentation/src
```
