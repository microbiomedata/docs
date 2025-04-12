# Developing NMDC software

Here's an overview of the tools and techniques NMDC team members use when developing NMDC software.

## Programming languages and frameworks

### Web application servers

We build web application servers using [Python](https://www.python.org/) and the [FastAPI](https://fastapi.tiangolo.com/) framework. We use [Swagger UI](https://swagger.io/tools/swagger-ui/) to render our [OpenAPI](https://www.openapis.org/) specifications as interactive API documentation.

_Examples: [nmdc-runtime](https://github.com/microbiomedata/nmdc-runtime) and [nmdc-server](https://github.com/microbiomedata/nmdc-server)_

### Web application clients

We build web application clients using [TypeScript](https://www.typescriptlang.org/), [Vue.js](https://vuejs.org/), and the [Vuetify](https://vuetifyjs.com/en/) component framework, as well as HTML and CSS.

_Example: [nmdc-server](https://github.com/microbiomedata/nmdc-server)_

### Mobile application clients

We build mobile application clients using [TypeScript](https://www.typescriptlang.org/), [React](https://react.dev/), the [Ionic](https://ionicframework.com/) mobile SDK, and the [Capacitor](https://capacitorjs.com/) runtime.

_Example: [nmdc-field-notes](https://github.com/microbiomedata/nmdc-field-notes)_

### Notebooks

We demonstrate things using [Jupyter](https://jupyter.org/) notebooks containing [Python](https://www.python.org/) and [R](https://www.r-project.org/) code.

_Example: [nmdc_notebooks](https://github.com/microbiomedata/nmdc_notebooks)_

### Configuration

We configure things using [YAML](https://yaml.org/) and [TOML](https://toml.io/en/).

_Examples: GitHub Actions and Python Poetry_

## Package/dependency management tools

### Python dependency management

In most of our Python projects, we use [Poetry](https://python-poetry.org/) to manage dependencies. While `pip-tools` is still in use in some repos, we are moving away from it (to Poetry).

_Examples: [nmdc-schema](https://github.com/microbiomedata/nmdc-schema) (Poetry), [refscan](https://github.com/microbiomedata/refscan)_

### TypeScript/JavaScript dependency management

For TypeScript/JavaScript projects, we use [npm](https://nodejs.org/) to manage dependencies. While [yarn](https://yarnpkg.com/) is still in use in one repository, we are not using any yarn-specific features there and may eventually move it to npm.

_Examples: [nmdc-field-notes](https://github.com/microbiomedata/nmdc-field-notes) (npm), [nmdc-server](https://github.com/microbiomedata/nmdc-server) (yarn)_

## Application deployment and artifact generation

### Make

We use [Make](https://www.gnu.org/software/make/) as a general purpose task runner in many projects. In addition to the typical use of defining output [target files](https://www.gnu.org/software/make/manual/html_node/Rule-Example.html) and their dependencies, we also make extensive use of [phony targets](https://www.gnu.org/software/make/manual/html_node/Phony-Targets.html). These allow a series of complex commands to be invoked by one simple `make` command.

_Examples: [nmdc-runtime](https://github.com/microbiomedata/nmdc-runtime) and [nmdc-schema](https://github.com/microbiomedata/nmdc-schema)_

### Docker

Projects which are designed to be run as deployed applications should be containerized (e.g., using [Docker](https://www.docker.com/)). This means that the repository, itself, should contain at least one [Dockerfile](https://docs.docker.com/get-started/docker-concepts/building-images/writing-a-dockerfile/). Once a Docker image has been built according to the Dockerfile, it can be pushed to a container registry (we use the [GitHub Container Registry](https://docs.github.com/en/packages/working-with-a-github-packages-registry/working-with-the-container-registry); i.e., GHCR). In a deployment environment, the appropriate image can be pulled from the container registry and instantiated as a Docker container.

For containerized applications, in addition to at least one Dockerfile, we typically include a [Docker Compose](https://docs.docker.com/compose/) file. This allows other containers necessary for local development (, a database, a static file server, etc.) to be run alongside the main application container.

_Examples: [nmdc-server](https://github.com/microbiomedata/nmdc-server), [nmdc-runtime](https://github.com/microbiomedata/nmdc-runtime)_

### Python Package Index (PyPI)

Python-based projects which are designed to be libraries that are consumed by other projects get deployed to the [Python Package Index](https://pypi.org/) (PyPI). In projects which are managed by Poetry, we use the functionality provided by Poetry to [build](https://python-poetry.org/docs/cli/#build) and [publish](https://python-poetry.org/docs/cli/#publish) the package.

_Examples: [nmdc-schema](https://github.com/microbiomedata/nmdc-schema) and [geoloc-tools](https://github.com/microbiomedata/geoloc-tools)_

### GitHub Actions

We use [GitHub Actions](https://docs.github.com/en/actions) for a variety of automation tasks. In general, we strive to automate as many tasks as possible. The things we do using GitHub Actions include:

- Running automated tests and code quality assessment tools
- Regenerating and deploying web-based documentation to [GitHub Pages](https://pages.github.com/)
- Deploying web applications to their hosting environments (e.g., NERSC Spin)
- Building and pushing container images to container registries (e.g., GHCR)
- Building and publishing Python packages to PyPI

_Examples: [nmdc-field-notes](https://github.com/microbiomedata/nmdc-field-notes), [submission-schema](https://github.com/microbiomedata/submission-schema), [docs](https://github.com/microbiomedata/docs)_

## Data pipelines and orchestration

There are a number of pipelines that produce data assets (e.g., JSON, XML files, etc.) and accomplish various ad-hoc tasks (like asset ingest, scheduled routine jobs, etc.) in the NMDC runtime framework. It's important that we have a one-stop shop for the orchestration of these data pipelines, and we use [Dagster](https://docs.dagster.io/) as our solution of choice for this problem.

_Repository: [nmdc-runtime](https://github.com/microbiomedata/nmdc-runtime)_

## Bioinformatics workflows

NMDC workflows use public repositories written in [Workflow Description Language](https://openwdl.org/) (WDL) and public Docker containers for software package management.

Here are the guidelines we follow when developing and using workflows.

### WDL

- Use WDL version 1.0
- Outputs are required and specified at the workflow level
- Workflows should be JAWS compatible including specifying database dependencies with `/refdata`
- Specify container versions in each WDL, ideally at the _task_ level
- Use `docker` in the `runtime` block ,and specify `time`, `cpu` and `memory`
  - If using a different container management tool like singularity and running outside of JAWS, specify that in the Cromwell configuration file
- Adhere to other JAWS [best practices for creating WDLs](https://jaws-docs.readthedocs.io/en/latest/Resources/best_practices.html)
- Use SHA or tagged versions for Docker containers
- [Sub-workflows](https://cromwell.readthedocs.io/en/latest/SubWorkflows/) should be imported using HTTPS imports from the appropriate GitHub repository
- Use `meta` block to specify maintainer, version, and email

### WDL validation

- Use [WOMtool](https://cromwell.readthedocs.io/en/stable/WOMtool/), [miniwdl](https://miniwdl.readthedocs.io/en/latest/), or [jaws validate](https://jaws-docs.readthedocs.io/en/latest/jaws/jaws_usage.html#specialty-commands) to confirm your WDL is valid; e.g., `miniwdl check --strict <wdl>`

### Docker containers

<!-- TODO: We link to Docker Hub here, while saying elsewhere that we use GHCR as our registry. Consider standardizing. -->

- Use organizational registries (e.g., https://hub.docker.com/u/microbiomedata), not personal ones

### Continuous integration/deployment (CI/CD)

- Use GitHub Actions to validate WDLs (e.g., [.github/workflows/wdl_linter.yml](https://github.com/microbiomedata/mg_annotation/blob/master/.github/workflows/wdl_linter.yml))

### Releases

- Use semantic versioning

## Development environments

We use [Docker](https://www.docker.com/) and [Docker Compose](https://docs.docker.com/compose/) to create local development environments. Specific setup instructions are included in the respective repository's documentation.

_Examples: [nmdc-runtime](https://github.com/microbiomedata/nmdc-runtime) and [nmdc-server](https://github.com/microbiomedata/nmdc-server)_

The general expectation is that the databases will be loaded locally. Database dumps are stored on the NERSC filesystem and can used to populate local instances.

Team members use a variety of text editors and IDEs when working with source code. Examples include Visual Studio Code and Jetbrains PyCharm.

## NMDC Schema design principles and LinkML usage

The NMDC Schema (i.e., `nmdc-schema`) describes data that are legal in NMDC's metadata store. It's written in [LinkML](https://linkml.io/) and its source files are accessible at [https://github.com/microbiomedata/nmdc-schema](https://github.com/microbiomedata/nmdc-schema).

It incorporates many elements from the GSC's [MIxS](https://github.com/GenomicsStandardsConsortium/mixs) standard, often imposing a higher level of structure.

The NMDC Submission Schema (i.e., `submission-schema`) is derived from NMDC Schema, frequently by flattening out slot ranges and applying stricter regular expression pattern constraints. In the future, some elements of `nmdc-schema` might be moved to live exclusively in `submission-schema`.

### Schema development and use

- The `nmdc-schema` is serialized as multiple YAML files. Those files live in the `src/schema` directory in the `nmdc-schema` repository.
- We currently have a highly modular schema with `imports`, but might switch to having just the `nmdc.yaml` and `mixs.yaml`
- If we decide to stick with a modular design, we should work towards getting the modules to compile independently
- Some slot constraints are expressed as `structured_pattern.syntax`. A version of the schema in which all modules have been merged—and in which the `structured_pattern.syntax`es have been converted into regular expressions—is available at [https://github.com/microbiomedata/nmdc-schema/blob/main/nmdc_schema/nmdc_materialized_patterns.yaml](https://github.com/microbiomedata/nmdc-schema/blob/main/nmdc_schema/nmdc_materialized_patterns.yaml)

#### Naming conventions

- Follow standard LinkML naming conventions (e.g., `UpperCamelCase` for classes and enums, `snake_case` for slots). Element names should not include whitespace
- Use LinkML linter to check style and conventions
- Class names should be nouns or noun-phrases (e.g., `Person`, `SequenceAlignment`, `Annotation`)
- Spell out abbreviations except for common terms (e.g., "DNA")
- Multivalued slots should be named as plurals
- Pre-existing elements may be "grandfathered in" with legacy naming

#### Class and slot design

<!-- Note: I was surprised to see the line about minimizing YAML comments. Maybe the idea is to use LinkML comments instead? -->

- Document all model elements with descriptions and textual annotations
- Include in-schema examples for all slots
- Provide valid examples for all classes in `src/data/valid` and invalid/counterexamples for all classes in `src/data/invalid`
- Use enums for categorical values (i.e., finite sets)
- Reuse existing schema elements whenever possible. For example, in our case, we found we don't need both a `soil_temp` slot and a separate `air_temp` slot
- Minimize the use of YAML `#` comments in the schema files
- The schema as a whole can have `comments`, `notes`, `todos`, `see_also`s, etc.
- New classes should be asserted as `is_a` subclasses of existing `nmdc-schema` classes
- Use `abstract: true` parent or grouping classes to define shared behavior and attributes
- `class_uri`s and `slot_uri`s must be asserted
- Include `aliases` for alternative terms to aid discoverability. Note: this is different from the `alias` slot, which should almost never be used.

#### ID and naming patterns

- Use `structured_pattern.syntax` for defining ID patterns
- The `{}` enclosed portions of `structured_pattern.syntax`es must be defined as regular expressions in the schema's `settings` section
- Identifiers should be permanent, unique, and ideally resolvable
- Register all new prefixes in the bioregistry

#### Schema structural integrity

- All classes must assert a `class_uri`
- Classes must use the `type` slot for consistent typing
- Inherited slots should not be reiterated in child classes

#### Deprecation practices

- Follow the two-stage deprecation process
- Include replacements with `deprecated_element_has_exact_replacement`
- Document deprecation with dates and issue references
- Move deprecated elements to the `deprecated.yaml` file

### Data validation and schema interaction

#### Schema access and manipulation

- Use LinkML's `SchemaView()` for programmatic schema access
- Iterating over the `attributes` (not `slots`) in an `induced_class` is a very common pattern

#### Resource access patterns

- Schema resources should be accessible through standardized getter methods
- Use package resources rather than file paths

#### Schema analysis and validation tools

- Create tools to identify unused schema elements
- Implement pattern linting for schema quality
- Build reports for subset usage and element coverage
- Create utilities to scrutinize schema elements
- Run validation during CI process

#### Validation standards

- Validate data using LinkML tools
- Data producers should validate their data
- Use Python data classes from the `nmdc-schema` Python package instead of generating dicts/JSON manually
- Schema definitions must be properly materialized
- Schema must support proper validation with key libraries
- Check documents against schema before submission

#### Slot grouping and organization

- Use LinkML's `is_grouping_slot` or `slot_group` for logical grouping
- `slot_group` can only relate a slot to one other slot,like `is_a`
- `in_subset` is another grouping option
- When introducing new grouping subsets, ensure that all applicable legacy slots are added
- Grouping structures require maintenance to avoid incomplete groups

#### Enum usage

- Create enums for categorical values
- Include `description`s and `meaning`s (ontology references) for permissible values
- Use `aliases` to support alternative terms
- The enum, itself, should include a `description` and other textual annotations

<!-- TODO: Consider moving these two sections to the previous parent section, which is about schema development. -->

#### Modularity

- Avoid/minimize circular imports between modules
- Use the LinkML linter routinely before merges

#### Design principles

- The use of `any_of.range`s and `rules` should be minimized in order to maximize compatibility with SQL, RDF, etc., representations of the schema and the data

## Database management systems

### MongoDB

We use [MongoDB](https://www.mongodb.com/) as the central metadata store for NMDC (meta)data. That central metadata store is the system of record. The NMDC API / Runtime provides programmatic access to the MongoDB backend. NMDC API queries access data from MongoDB.

### PostgreSQL

We use [PostgreSQL](https://www.postgresql.org/) (i.e., Postgres) for the NMDC [Data portal](https://data.microbiomedata.org/) and [Submission portal](https://data.microbiomedata.org/submission/home).

We use [SQLAlchemy](https://www.sqlalchemy.org/) to manage data migrations in Postgres.

The Postgres database is not a system of record for NMDC (meta)data. For the most part, it is a transformed copy of the system of record from MongoDB, transformed into a relational schema optimized for the kinds of queries that the Data Portal client makes.

The Submission Portal uses the Postgres database to store submission information before that information gets ingested into the MongoDB database.

## Testing

To test Python code, we use the [pytest](https://docs.pytest.org/) test framework. In addition, in some projects, we use the [pytest-cov](https://pypi.org/project/pytest-cov/) package to measure code coverage, which we use to determine which parts of the codebase the tests cover.

To test TypeScript/JavaScript code, we use the [Vitest](https://vitest.dev/) test framework. We also sometimes use [Storybook](https://storybook.js.org/) to preview UI components in isolation.

## Documentation and communication

We try to keep in mind that source code is generally read more often than it is written. We try to make it easy for the next person that looks at the code we write, to understand what we were thinking when we wrote it.

In code, we try to document each function, including indicating the data types of its parameters and return value. For recursive functions and other complex code, we err on the side of including more documentation than may be necessary, in an attempt to help the reader along.

Also, we try to include a README.md file in the root directory of each repository. That file usually contains the name of the project, a high-level summary of the contents of the repo, instructions for using the contents of the repo, and instructions for contributing to the repo.

For diagramming, we usually use either Mermaid or diagrams.net (draw.io).

<!-- TODO: Add something about issues and PRs. -->

## Use of Large Language Models (LLMs)

This is a new and fast evolving area. NMDC staff have experience using the following tools for code generation and coding and writing assistance:

- [ChatGPT](http://chatgpt.com/)
- [Claude](https://claude.ai/)
- [Github Copilot](https://github.com/features/copilot)
- [Gemini](https://gemini.google.com/)

LBNL employees have access to the [CBORG](https://cborg.lbl.gov/) system, which provides access to several commercial and internally-hosted LLMs.

## Git and GitHub

All code being developed in the NMDC ecosystem/toolchain is open sourced and all repositories are made publicly accessible via GitHub, under the [microbiomedata](https://github.com/microbiomedata/) organization. By choosing GitHub as our code collaboration platform of choice, we are marrying ourselves to [Git](https://git-scm.com/doc) as our de facto version control tool. We follow the typical Git/GitHub workflow for getting "new code" (for bug fixes, feature enhancements, etc.) into our codebase which is: create an issue for your request → make a corresponding branch → add your commits to that branch → make a PR which will be reviewed by "owners" (experts) → merge into `main` → delete branch. Releases for the various repositories are also coordinated/managed via [GitHub Releases](https://docs.github.com/en/repositories/releasing-projects-on-github/about-releases) by following a thoroughly documented and standardized “release process”.

## DevOps and infrastructure

The CI/CD framework used to automate processes like package/codebase deployments, running test suite regressions/new tests, etc., are all managed/maintained using [GitHub Actions](https://github.com/features/actions).

## Data management

### JAMO

We use the JGI Archive and Metadata Organizer (JAMO) system for data lifecycle management to store copies of our data on tape on the [NERSC HPSS](https://docs.nersc.gov/filesystems/archive/) system. This allows for efficiently storing related workflow products on tape, and gives us an offline canonical copy of the data.

### Globus

We use [Globus](https://www.globus.org/) to enable managed, high-performance, bulk data [access to NMDC data](https://docs.microbiomedata.org/howto_guides/globus.html).

### Database backups

Database backups are performed nightly at NERSC using Kubernetes CronJobs that invoke shell scripts that use standard programs (e.g., `mongodump` and `pg_dump`) to dump the databases to files, which are then stored on the NERSC filesystem.

## Code quality and maintainability

We encourage the use of [black](https://github.com/psf/black), a highly configurable Python code formatter, on our Python codebases. It helps ensure consistent formatting, making the code easier to read and maintain.

Another tool we use to check [PEP8](https://peps.python.org/pep-0008/) compliance is [flake8](https://flake8.pycqa.org/en/latest/).

We have, however, started porting over some of our repositories to use [ruff](https://github.com/astral-sh/ruff), which is a linter and formatter for Python. It might become our de facto code quality and maintainability checker in the future.

Some tools that we use for type checking are [mypy](https://github.com/python/mypy) (for static type checking) and [Pydantic](https://github.com/pydantic/pydantic) (for data validation using Python type hints).

## Code review

Each of the repositories in the [microbiomedata](https://github.com/microbiomedata/) organization has a "product owner" (or experts who contribute to the repositories frequently) who can either be requested explicitly for code/pull request reviews, or if the PR is lingering around on the repository for long enough it will be picked up by one of the experts who contributes to the repository.

The expert will review the code changes and appropriately leave helpful comments, request for specific code changes, or approve the PR.

Once a PR has been signed off on ("approved") it can be merged in, either by the creator of the PR or by the expert who approved it.

## Release process

For our public-facing deployed applications (namely, `nmdc-server` and `nmdc-runtime`) we have a monthly release cadence. Since both of these applications rely on the schema and need to use the same schema version, we also take nmdc-schema into account in the monthly releases. The overall process is:

- During normal development of `nmdc-server` and `nmdc-runtime`, as changes are merged into the `main` branch they are deployed automatically to our dev environment
- Approximately a week before the target release date, we ensure that a new version of `nmdc-schema` has been released and that both `nmdc-runtime` and `nmdc-server` depend upon that version of `nmdc-schema`. During this week, we test the applications in the dev environment and are more selective about which changes we merge into those repositories' `main` branches.
- On the release day, we create [GitHub Releases](https://docs.github.com/en/repositories/releasing-projects-on-github/managing-releases-in-a-repository) with associated [semantic version](https://semver.org/) tags (e.g., `v2.0.3`) from the `main` branches of both `nmdc-server` and `nmdc-runtime`. This triggers a deployment of the code from those tags to the production environment.
