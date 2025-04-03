# Developing NMDC software

Here's an overview of the tools and techniques NMDC team members use when developing NMDC software.

## Programming languages and frameworks

### Web application servers

We build **web application servers** using [Python](https://www.python.org/) and the [FastAPI](https://fastapi.tiangolo.com/) framework. We use [Swagger UI](https://swagger.io/tools/swagger-ui/) to render our [OpenAPI](https://www.openapis.org/) specifications as interactive API documentation.

> Examples: [NMDC Runtime API](https://github.com/microbiomedata/nmdc-runtime) and [NMDC Data Portal](https://github.com/microbiomedata/nmdc-server)

### Web application clients

We build **web application clients** using [TypeScript](https://www.typescriptlang.org/), [Vue.js](https://vuejs.org/), and the [Vuetify](https://vuetifyjs.com/en/) component framework, as well as HTML and CSS. 

> Example: [NMDC Data Portal](https://github.com/microbiomedata/nmdc-server)

### Mobile application clients

We build **mobile application clients** using [TypeScript](https://www.typescriptlang.org/), [React](https://react.dev/), the [Ionic](https://ionicframework.com/) mobile SDK, and the [Capacitor](https://capacitorjs.com/) runtime. 

> Example: [NMDC Field Notes](https://github.com/microbiomedata/nmdc-field-notes)

### Notebooks

We demonstrate things using [Jupyter](https://jupyter.org/) **notebooks** containing [Python](https://www.python.org/) and [R](https://www.r-project.org/) code. 

> Example: [NMDC Notebooks](https://github.com/microbiomedata/nmdc_notebooks)

### Configuration

We **configure** things using [YAML](https://yaml.org/) and [TOML](https://toml.io/en/).

> Examples: GitHub Actions and Python Poetry

<!--
TODO: What about Bash and WDL, which I think are both used for bioinformatics workflows?
-->

## Package/Dependency Management Tools

- **Poetry** (nmdc-schema)
- **Pip / piptools** (nmdc-runtime)
- **Python venv?** (??) (used when we're using pip in runtime)

## Application Deployment Tools, Artifact Generation

- **Make/makefiles**, **GitHub Actions**, **bash**, **Docker**
- **Packaging** our tools
- Deployment to **PyPI**

## Data Pipeline/Orchestration Frameworks

- **Dagster** (`nmdc-runtime`)
- **cron** (`nmdc-server`?)

## Bioinformatics Workflows

- **WDL version 1.0** + docker containers
- **Github actions** for linting with miniwdl
- User facility coordination best practices document (link out to this)

## Development Environments

- "How to get up and running locally for development"

<!-- TODO: What about code editor software; e.g. PyCharm, VS Code, Vim -->

<!-- TODO: What about database clients; e.g. Mongo Compass, pgAdmin, Beekeeper Studio, DataGrip -->

## Schema/Data Model Development Framework – LinkML

- We use **LinkML**, as opposed to... writing SQL schemas directly?
- Validation via **JSONSchema**

## Database Management Systems

- **PostgreSQL**
- **MongoDB**

## Testing

- **Python**: Pytest
- **JavaScript/TypeScript**: Jest, (maybe Cypress?) (Playwright?) (Storybook?)

## Documentation & Communication

- `...`

## Bonus Topic: Use of LLMs Across Repositories

- **ChatGPT**, **Claude**, **Claude Code**, **Gemini**

## Git & GitHub

- Codebase management and version control (VCS)
- Default GH setup config 
- A flow: Issue -> Branch -> commits -> PR -> Review -> merge
- Creating Releases
- PR process
- GHA workflow configuration

## Dev-Ops / Infrastructure

- **CI/CD & Release Processes**
- **Containerization** (Docker, Kubernetes, Helm)
- **Cloudflare**, **Spin** etc.
- Note: May move stuff here from `infra-admin` repo

## Code Quality & Maintainability

- **Linting** – flake8
- **Formatting** – black
- **Type checking** (mypy, pydantic?, SQLAlchemy?)

## Code Review

- Roles and who / when to request 
- Types of feedback and timeline
- Who can do the final merge if it’s a PR

## Release Process Best Practices

- **Versioning**: Use semantic version
