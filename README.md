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
      * [Maintenance](#maintenance)
        * [Procedure: Basic (to edit 1 file)](#procedure-basic-to-edit-1-file)
        * [Procedure: Intermediate (to edit 1+ files)](#procedure-intermediate-to-edit-1-files)
    * [Legacy content](#legacy-content)
      * [NMDC documentation](#nmdc-documentation)
        * [Omissions](#omissions)
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
   1. `nmdc`: Current content (under construction), initialized as a copy of the legacy content
2. `./legacy`: Legacy content we include in the website to support legacy references/publications
3. `./src`: Code we use to compile local and remote content into a website
4. `./`: Repository-level configuration files and documentation

### Content

The `./content/nmdc` directory contains our current documentation that is not pulled from an external repository.
This directory began as a 1-to-1 copy of the `./legacy/nmdc-documentation` directory. The latter is, itself, mostly a
copy of the `NMDC_documentation` repository (more details about this are in the "Legacy content" section below).

Unlike the contents of the `./legacy/nmdc-documentation` directory, the contents of the `./content/nmdc` directory will
continue to change over time; i.e. NMDC team members will update and add documentation to this directory.

#### Maintenance

This documentation is implemented within the [Sphinx](https://www.sphinx-doc.org) framework.
The content is organized according to the
[Diátaxis](https://diataxis.fr/how-to-use-diataxis/#use-diataxis-as-a-guide-not-a-plan) guidelines.

Here's how you can make (technically, "propose") changes to this documentation:

> **Note:** The high-level process may be familiar to you: (1) create a GitHub Issue, (2) create a branch associated
> with that Issue, (3) make changes on that branch, and (4) create a Pull Request to merge that branch into `main`.
> You can use whatever workflow you want in order to follow that process. The following are some example workflows:

##### Workflow: Basic (to edit 1 file)

1. Create a GitHub Issue describing what you want to change (e.g. "Fix Foo in Bar")
2. On GitHub, go to the file within `./content/nmdc/src` that you want to edit
3. Click the "Edit this file" button (i.e. the pencil icon button) at the upper right
4. Edit the file
5. Click the "Commit changes..." button at the upper right
6. Customize the commit message to tell others what you did (e.g. "`Fix typo in link`")
7. Mark the bubble that says "**Create a new branch** for this commit and start a pull request"
8. (Recommended) Customize the branch name so it starts with the GitHub Issue number (e.g. `123-fix-foo-in-bar`)
9. Click "Propose changes"
10. Fill in the Pull Request form and click "Create pull request"

You will end up with a Pull Request (PR) containing the changes. Once the PR gets merged into `main`,
the documentation website will automatically be updated to reflect the changes.

##### Workflow: Intermediate (to edit 1+ files)

1. Create a GitHub Issue describing what you want to change (e.g. "Fix Foo in Bar")
2. Visit https://github.dev/microbiomedata/docs/
3. Click the branch name (e.g. `main`) at the lower left
4. Click "Create a new branch..." at the top
5. Enter a name for the branch, beginning with an issue number (e.g. `123-fix-foo-in-bar`)
6. (If prompted) Click "Switch to Branch"
7. Make changes in `./content/nmdc/src`
8. Click the "Source Control" icon in the left sidebar (3rd from the top)
9. Hover over the "Changes" heading and click the `+` icon that appears
10. Enter a commit message to tell others what you did (e.g. "`Fix typo in link`")
11. Click the "Commit & Push" button
12. Visit https://github.com/microbiomedata/docs/ and create a Pull Request for that branch

You will end up with a Pull Request (PR) containing the changes. Once the PR gets merged into `main`,
the documentation website will automatically be updated to reflect the changes.

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

That will start up several Docker containers, which you can access via the URLs below:

- http://localhost:5000 - the home page of the website
- http://localhost:5001 - the legacy documentation portion of the website
- http://localhost:5002 - the current documentation portion of the website

In addition, whenever you make changes to content,
the associated section of the associated website will automatically be rebuilt
(at which point, you can refresh your web browser to see the newly-rebuilt section).

# TODO

- [ ] Populate the "TODO" sections above
- [ ] Update legacy `requirements.txt` files to indicate specific versions
- [ ] Implement a framework for pulling in content from external sources
- [ ] Migrate `.rst` files into Markdown (`.md`)
