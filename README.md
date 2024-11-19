# Docs

> [!NOTE]  
> This repository is in early development.
> We are currently in the process of reviewing, pruning, and consolidating our documentation.

## Introduction

This repository contains the content that we compile into our
[documentation website](https://microbiomedata.github.io/docs).

## Table of contents

<!-- TOC -->
* [Docs](#docs)
  * [Introduction](#introduction)
  * [Table of contents](#table-of-contents)
  * [Repository structure](#repository-structure)
    * [Content](#content)
    * [Legacy content](#legacy-content)
      * [NMDC documentation](#nmdc-documentation)
        * [Omissions](#omissions)
        * [Maintenance](#maintenance)
          * [Prerequisites](#prerequisites)
          * [Procedure: Basic (to edit 1 file)](#procedure-basic-to-edit-1-file)
          * [Procedure: Intermediate (to edit 1+ files)](#procedure-intermediate-to-edit-1-files)
    * [Code](#code)
    * [Repository-level configuration files and documentation](#repository-level-configuration-files-and-documentation)
      * [GitHub Actions](#github-actions)
  * [Development](#development)
    * [Spin up the development environment](#spin-up-the-development-environment)
* [TODO](#todo)
<!-- TOC -->

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

In addition to the files we copied, the directory also contains some files that are _exclusive_ to this repository;
e.g., `Dockerfile` and `.gitignore`.


##### Omissions

When copying the aforementioned files from the `NMDC_documentation` repository, we _omitted_ the following files:

- Schema element documentation in `docs/reference/metadata`
- Schema-related images in `docs/_static/images/reference/metadata`
- Schema in `docs/_static/jsonschema`

Instead of maintaining a local copy of that documentation here, we redirect visitors to the _standalone_
[schema documentation](https://microbiomedata.github.io/nmdc-schema/).

> **Example:** When someone visits `/reference/metadata/xylene.html` on this documentation website,
> they'll be automatically redirected to https://microbiomedata.github.io/nmdc-schema/xylene/. This redirection
> is configured in `legacy/nmdc-documentation/src/conf.py`.

You can compare the `legacy/nmdc-documentation/src` directory with the corresponding directory in the
upstream repository, by following these steps:

```shell
# Clone the upstream repository onto your computer.
git clone https://github.com/microbiomedata/NMDC_documentation.git /tmp/NMDC_documentation

# Use Git to compare the corresponding directories. 
git diff --stat /tmp/NMDC_documentation/docs ./legacy/nmdc-documentation/src
```

##### Maintenance

This documentation is implemented within the [Sphinx](https://www.sphinx-doc.org) framework.
The content is organized according to the [Diátaxis](https://diataxis.fr/how-to-use-diataxis/#use-diataxis-as-a-guide-not-a-plan) guidelines.

Here's how you can propose changes to this documentation:

> Note: The general flow is: (1) create a GitHub Issue, (2) create a branch associated with that Issue,
> (3) make changes on that branch, and (4) create a Pull Request to merge that branch into the `main` branch.
> The following are a couple of the many ways someone can do those things (other ways are also OK).

###### Prerequisites

1. Create a GitHub Issue describing what you want to change (e.g. "Fix Foo in Bar")

###### Procedure: Basic (to edit 1 file)

1. On GitHub, go to the file within `legacy/nmdc-documentation/src/` that you want to edit
2. Click the "Edit this file" button (i.e. the pencil icon button) at the upper right
3. Edit the file
4. Click the "Commit changes..." button at the upper right
5. Customize the commit message to tell others what you did (e.g. "`Fix typo in link`")
6. Mark the bubble that says "**Create a new branch** for this commit and start a pull request"
7. (Recommended) Customize the branch name so it starts with the GitHub Issue number (e.g. `123-fix-foo-in-bar`)
8. Click "Propose changes"
9. Fill in the Pull Request form and click "Create pull request"

You will end up with a Pull Request (PR) containing the changes. Once the PR gets merged into `main`,
the documentation website will automatically be updated to reflect the changes.

###### Procedure: Intermediate (to edit 1+ files)

1. Visit https://github.dev/microbiomedata/docs/
2. Click the branch name (e.g. `main`) at the lower left
3. Click "Create a new branch..." at the top
4. Enter a name for the branch, beginning with an issue number (e.g. `123-fix-foo-in-bar`)
5. (If prompted) Click "Switch to Branch"
6. Make changes in `legacy/nmdc-documentation/src`
7. Click the "Source Control" icon in the left sidebar (3rd from the top)
8. Hover over the "Changes" heading and click the `+` icon that appears
9. Enter a commit message to tell others what you did (e.g. "`Fix typo in link`")
10. Click the "Commit & Push" button
11. Visit https://github.com/microbiomedata/docs/ and create a Pull Request for that branch

You will end up with a Pull Request (PR) containing the changes. Once the PR gets merged into `main`,
the documentation website will automatically be updated to reflect the changes. 

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
- [ ] Update legacy `requirements.txt` files to indicate specific versions
- [ ] Implement a framework for pulling in content from external sources
- [ ] Configure a vanity URL once we have a cohesive website
- [ ] Migrate `.rst` files into Markdown (`.md`)
