# Developing NMDC Software

This page is under construction.

## Programming Languages and Frameworks

- **Python** (versions vary between projects currently)
- **Web app development frameworks**
- **API development frameworks**: FastAPI / Swagger / OpenAPI
- **JS/TS**: Front end web: Vue (`nmdc-server`) and React (`nmdc-field-notes`)
- **Bash and WDL** for workflows?
- **Mobile app development frameworks**: Ionic & Capacitor (`nmdc-field-notes`)
- **Jupyter notebooks**

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
