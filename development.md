# Development

## Introduction

This document contains information about the infrastructure aspect of the documentation website,
as opposed to the content aspect.

## Table of contents

<!-- TOC -->
* [Development](#development)
  * [Introduction](#introduction)
  * [Table of contents](#table-of-contents)
  * [Local development](#local-development)
    * [Spin up the development environment](#spin-up-the-development-environment)
    * [Applying changes](#applying-changes)
      * [Home section](#home-section)
      * [Runtime section](#runtime-section)
      * [Workflow docs](#workflow-docs)
  * [Deployment](#deployment)
  * [Google Analytics](#google-analytics)
<!-- TOC -->

## Local development

This section is about running an instance of the website locally.

### Spin up the development environment

Assuming you have Docker installed, you can spin up the development environment by running: 

```shell
docker compose up --detach
```

That will start up several Docker containers, which you can access via the URLs below:

- http://localhost:9000 - the entire website
- http://localhost:9001 - only the Home section of the website
- http://localhost:9002 - only the Runtime section of the website
- http://localhost:9003 - only the Workflows section of the website

### Applying changes

#### Home section

Whenever you update files in the `content/home/src` directory,
the Home section of the website will be automatically rebuilt.
Refresh your web browser to see that newly-rebuilt section of the website.

#### Runtime section

Nothing will automatically happen in the development environment when someone
updates files in the **upstream** Runtime repository. To adopt those changes
in the development environment, rebuild the `runtime-docs` container
by issuing the following sequence of commands:

```shell
docker compose down             runtime-docs
docker compose build --no-cache runtime-docs
docker compose up --detach      runtime-docs
```

If you **only** make changes to the documentation source files that reside in _this_ repository
(i.e. those in `pullers/runtime_docs`), then you can issue this sequence of commands instead,
which will allow Docker to _avoid refetching_ the source files from the upstream repo:

```shell
docker compose down             runtime-docs
docker compose build            runtime-docs
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

## Deployment

The `.github/workflows` directory contains YAML files that we use to configure GitHub Actions.
We use GitHub Actions to (a) compile local and remote content into a single website,
and to (b) publish that single website to GitHub Pages.

## Google Analytics

We use Google Analytics to collect and analyze website traffic. You can search the repository for
our Google Analytics Property ID (i.e. "`G-VH6HKVLCWN`") in order to learn more.
