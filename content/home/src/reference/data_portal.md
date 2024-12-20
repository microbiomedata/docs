# NMDC Data Portal

The NMDC Data Portal is a web application researchers can use to discover and access standardized multi-omics microbiome data.

The main technologies upon which it is built are:

* [Python](https://www.python.org/) and [FastAPI](https://fastapi.tiangolo.com/)
* [PostgreSQL](https://www.postgresql.org/) and [SQLAlchemy](https://www.sqlalchemy.org/)
* [Celery](https://docs.celeryq.dev/) and [Redis](https://redis.io/)
* [Vue.js](https://v2.vuejs.org/) and [Vuetify](https://v2.vuetifyjs.com/)

For specific versions  of these technologies currently being used by the NMDC Data Portal, see the Dependencies below.

### Dependencies

The NMDC Data Portal depends upon various Python and JavaScript libraries, which are listed in either of the following documents:

* [Python dependencies](https://github.com/microbiomedata/nmdc-server/blob/main/pyproject.toml)
* [Javascript dependencies](https://github.com/microbiomedata/nmdc-server/blob/main/web/package.json)

## Architecture

![nmdc-diagram](../_static/images/reference/data_portal/nmdc-diagram.svg)

## API documentation

In addition to providing a web-based GUI (graphical user interface), the NMDC Data Portal also exposes an HTTP API. Researchers can use the latter to _programmatically_ discover and access standardized multi-omics microbiome data.

Information about the HTTP API is in this [wiki](https://github.com/microbiomedata/nmdc-server/wiki/Search-API-Docs).

## Development documentation

Here are some resources people can use to learn about the development of the NMDC Data Portal.

* [Server and client development documentation](https://github.com/microbiomedata/nmdc-server/blob/main/docs/development.md)
* [Client architecture notes](https://github.com/microbiomedata/nmdc-server/blob/main/web/README.md)