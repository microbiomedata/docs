# Home

This directory contains files related to building the Home section of the website.

On April 11, 2025, we switched this section of the website from using the [Sphinx](https://www.sphinx-doc.org/) framework
with the [Read the Docs](https://sphinx-rtd-theme.readthedocs.io/) theme, to using the [MkDocs](https://www.mkdocs.org/) framework
with the [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/) theme.

## The `src` directory

Most of the files in `src` are files that we copied from
[commit `e0001a90`](https://github.com/microbiomedata/NMDC_documentation/commit/e0001a90f0b8ab4ee760ae9e63bb3b03bb38398f)
in the [NMDC_documentation](https://github.com/microbiomedata/NMDC_documentation) repository.
That was the latest commit on the `main` branch as of August 28, 2024.

### Omissions

When copying the aforementioned files from the `NMDC_documentation` repository, we _omitted_ the following files (the
paths shown here are relative to the root directory of _that_ repository):

- Schema element documentation in `docs/reference/metadata`
- Schema-related images in `docs/_static/images/reference/metadata`
- Schema in `docs/_static/jsonschema`

You can compare the `.src/` directory with the corresponding directory in the
upstream repository, by issuing these commands from the **root directory** of _this_ repository:

```shell
# Clone the upstream repository onto your computer.
git clone https://github.com/microbiomedata/NMDC_documentation.git /tmp/NMDC_documentation

# Use Git to compare the corresponding directories. 
git diff --stat /tmp/NMDC_documentation/docs ./content/home/src
```
