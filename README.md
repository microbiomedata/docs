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
        * [Basic workflow (to edit 1 file)](#basic-workflow-to-edit-1-file)
        * [Intermediate workflow (to edit 1+ files)](#intermediate-workflow-to-edit-1-files)
    * [Legacy content](#legacy-content)
    * [Code](#code)
    * [Repository-level configuration files and documentation](#repository-level-configuration-files-and-documentation)
      * [GitHub Actions](#github-actions)
  * [Development](#development)
    * [Spin up the development environment](#spin-up-the-development-environment)
    * [Watch for changes](#watch-for-changes)
      * [Legacy home docs](#legacy-home-docs)
      * [Home docs](#home-docs)
      * [Runtime docs](#runtime-docs)
      * [Workflow docs](#workflow-docs)
* [TODO](#todo)
<!-- TOC -->

## Repository structure

This repository has the following sections:

> [!NOTE]
> TODO

### Content

The `./content/home` directory contains our current documentation that is not pulled from an external repository.
This directory began as a 1-to-1 copy of the `./content/legacy_home` directory. The latter is, itself, mostly a
copy of the `NMDC_documentation` repository (more details about this are in the "Legacy content" section below).

Unlike the contents of the `./content/legacy_home` directory, the contents of the `./content/home` directory will
continue to change over time; i.e. NMDC team members will update and add documentation to this directory.

#### Maintenance

This documentation is implemented within the [Sphinx](https://www.sphinx-doc.org) framework.
The content is organized according to the
[Diátaxis](https://diataxis.fr/how-to-use-diataxis/#use-diataxis-as-a-guide-not-a-plan) guidelines.

Here's how you can make (technically, "propose") changes to this documentation:

> **Note:** The high-level process may be familiar to you: (1) create a GitHub Issue, (2) create a branch associated
> with that Issue, (3) make changes on that branch, and (4) create a Pull Request to merge that branch into `main`.
> You can use whatever workflow you want in order to follow that process. The following are some example workflows:

##### Basic workflow (to edit 1 file)

1. Create a GitHub Issue describing what you want to change (e.g. "Fix Foo in Bar")
2. On GitHub, go to the file within `./content/home/src` that you want to edit
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

##### Intermediate workflow (to edit 1+ files)

1. Create a GitHub Issue describing what you want to change (e.g. "Fix Foo in Bar")
2. Visit https://github.dev/microbiomedata/docs/
3. Click the branch name (e.g. `main`) at the lower left
4. Click "Create a new branch..." at the top
5. Enter a name for the branch, beginning with an issue number (e.g. `123-fix-foo-in-bar`)
6. (If prompted) Click "Switch to Branch"
7. Make changes in `./content/home/src`
8. Click the "Source Control" icon in the left sidebar (3rd from the top)
9. Hover over the "Changes" heading and click the `+` icon that appears
10. Enter a commit message to tell others what you did (e.g. "`Fix typo in link`")
11. Click the "Commit & Push" button
12. Visit https://github.com/microbiomedata/docs/ and create a Pull Request for that branch

You will end up with a Pull Request (PR) containing the changes. Once the PR gets merged into `main`,
the documentation website will automatically be updated to reflect the changes.

### Legacy content

See [content/legacy_home/README.md](./content/legacy_home/README.md).

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
docker compose up --detach
```

That will start up several Docker containers, which you can access via the URLs below:

- http://localhost:5000 - the entire website
- http://localhost:5001 - only the legacy home docs portion of the website
- http://localhost:5002 - only the home docs portion of the website
- http://localhost:5003 - only the Runtime docs portion of the website
- http://localhost:5004 - only the workflow docs portion of the website

### Watch for changes

#### Legacy home docs

Whenever you update files in the `content/legacy_home/src` directory,
the legacy home docs portion of the website will be automatically rebuilt.
Refresh your web browser to see that newly-rebuilt portion of the website.

#### Home docs

Whenever you update files in the `content/home/src` directory,
the home docs portion of the website will be automatically rebuilt.
Refresh your web browser to see that newly-rebuilt portion of the website.

#### Runtime docs

Nothing will automatically happen in the development environment when someone
updates files in the **upstream** Runtime repository. To adopt those changes
in the development environment, rebuild the `runtime-docs` container
by issuing the following sequence of commands:

```shell
docker compose down             runtime-docs
docker compose build --no-cache runtime-docs
docker compose up --detach      runtime-docs
```

#### Workflow docs

Nothing will automatically happen in the development environment when someone
updates files in the **upstream** workflow repositories. To adopt those changes
in the development environment, rebuild the `workflow-docs` container
by issuing the following sequence of commands:

```shell
docker compose down             workflow-docs
docker compose build --no-cache workflow-docs
docker compose up --detach      workflow-docs
```

If you **only** make changes to the documentation source files that reside in _this_ repository
(i.e. those in `pullers/workflow_docs`), then you can issue this sequence of commands instead,
which will allow Docker to _avoid refetching_ the source files from the upstream repos:

```shell
docker compose down             workflow-docs
docker compose build            workflow-docs
docker compose up --detach      workflow-docs
```

# TODO

- [ ] Populate the "TODO" sections above
- [ ] Update legacy `requirements.txt` files to indicate specific versions
