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
    * [Automatic deployment](#automatic-deployment)
    * [Manual regeneration and deployment (step-by-step)](#manual-regeneration-and-deployment-step-by-step)
    * [Workflow details (for GitHub Actions users)](#workflow-details-for-github-actions-users)
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

### Automatic deployment

Website regeneration and deployment happens automatically when a commit is pushed to the `main` branch of this repository.
The workflow that performs this is `.github/workflows/deploy-to-gh-pages.yml` ("Deploy to GitHub Pages").

### Manual regeneration and deployment (step-by-step)

Use this procedure when you need to regenerate and redeploy the website without creating a new commit on `main`.

1. Open the repository's **Actions** tab: https://github.com/microbiomedata/docs/actions
2. In the left sidebar, click **Deploy to GitHub Pages**
3. Click **Run workflow**
4. In the **Use workflow from** dropdown, select `main` (recommended for production)
5. Click the green **Run workflow** button to start the run
6. Open the new workflow run and monitor the jobs until they complete
7. Confirm both jobs succeeded:
   - **Assemble website**
   - **Deploy website**
8. Wait ~3 minutes, then verify the live site was refreshed: https://docs.microbiomedata.org

If the run fails, open the failed job, review the logs, fix the root cause, and run the workflow again.

### Workflow details (for GitHub Actions users)

The deployment path is:

1. `Deploy to GitHub Pages` (`deploy-to-gh-pages.yml`) is triggered (`push` to `main` or `workflow_dispatch`)
2. It calls `Assemble website` (`assemble-website.yml`)
3. `Assemble website` calls these reusable workflows in parallel:
   - `compile-home-docs.yml`
   - `fetch-and-compile-runtime-docs.yml`
   - `fetch-and-compile-workflow-docs.yml`
4. The assembled `github-pages` artifact is link-checked (`check-links.yml`)
5. `actions/deploy-pages` publishes the artifact to GitHub Pages

## Google Analytics

We use Google Analytics to collect and analyze website traffic. You can search the repository for
our Google Analytics Property ID (i.e. "`G-VH6HKVLCWN`") in order to learn more.
