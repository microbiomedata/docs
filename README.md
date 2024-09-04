# Docs

> [!NOTE]  
> This repository is in early development.
> We are currently in the process of reviewing, pruning, and consolidating our documentation.

## Introduction

This repository contains the content that we compile into our
[documentation website](https://microbiomedata.github.io/docs).

## Repository structure

This repository has the following sections:

1. `./content`: Current, high-level content about NMDC
2. `./legacy`: Legacy content we include in the website to support legacy references/publications
3. `./src`: Code we use to compile local and remote content into a website
4. `./`: Repository-level configuration files and documentation

### Content

> [!NOTE]  
> TODO

### Legacy content

#### NMDC documentation

Most of the files in the `legacy/nmdc-documentation` directory are files that we copied from
[commit `8786ff5a`](https://github.com/microbiomedata/NMDC_documentation/commit/8786ff5a63be21d38e8a01cce6f4fecc073526ac)
in the [NMDC_documentation](https://github.com/microbiomedata/NMDC_documentation) repository.
That was the latest commit on the `main` branch as of August 28, 2024.
This documentation is implemented within the [Sphinx](https://www.sphinx-doc.org) documentation framework.

In addition to the files we copied, the directory also contains some files that are _exclusive_ to this repository;
e.g., `Dockerfile` and `.gitignore`.

##### Omissions

When copying the aforementioned files from the `NMDC_documentation` repository, we _omitted_ the following files:

- Schema element documentation in `src/reference/metadata`
- Schema-related images in `src/_static/images/reference/metadata`
- Schema in `src/_static/jsonschema`

Instead of maintaining a local copy of that documentation here, we redirect visitors to the _standalone_
[schema documentation](https://microbiomedata.github.io/nmdc-schema/).

> **Example:** When someone visits `/reference/metadata/xylene.html` on this documentation website,
> they'll be automatically redirected to https://microbiomedata.github.io/nmdc-schema/xylene/. This redirection
> is configured in `legacy/nmdc-documentation/src/conf.py`.

#### Workflow documentation

> [!NOTE]  
> TODO

### Code

> [!NOTE]  
> TODO

### Repository-level configuration files and documentation

- `.github/workflows`: GitHub Actions workflows
- `docker-compose.yml`: Specification for a _set_ of container images you can use when editing _any_ section of our documentation website
- `README.md`: This document

#### GitHub Actions

The `.github/workflows` directory contains YAML files that we use to configure GitHub Actions.
We use GitHub Actions to (a) compile local and remote content into a website,
and to (b) publish that website to the Internet.

## Development

### Spin up the development environment

Assuming you have Docker installed, you can spin up the development environment by running: 

```shell
docker compose up
```

That will run a web server, serving the legacy section of the website at the following URL:

- http://localhost:50000

In addition, whenever you make changes to content,
the associated sections of the website will automatically be rebuilt
(at which point, you can refresh your web browser to see the newly-rebuilt sections).

# TODO

- [ ] Populate the "TODO" sections above
- [ ] Include a snapshot of https://github.com/microbiomedata/workflow_documentation (https://nmdc-workflow-documentation.readthedocs.io) in the "Legacy" section
- [ ] Implement an overall website, of which the "Legacy" section is only one part
- [ ] Implement a framework for pulling in content from external sources
- [ ] Configure a vanity URL once we have a cohesive website
- [ ] Migrate `.rst` files into Markdown (`.md`)
