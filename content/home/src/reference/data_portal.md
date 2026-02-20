# NMDC Data Portal

The NMDC Data Portal is a web application researchers can use to discover and access standardized multi-omics microbiome data.

The main technologies upon which it is built are:

- [Python](https://www.python.org/) and [FastAPI](https://fastapi.tiangolo.com/)
- [PostgreSQL](https://www.postgresql.org/) and [SQLAlchemy](https://www.sqlalchemy.org/)
- [Vue.js](https://vuejs.org/) and [Vuetify](https://vuetifyjs.com/)

For specific versions of these technologies currently being used by the NMDC Data Portal, see the dependency lists linked below.

## Dependencies

The NMDC Data Portal depends upon various Python and JavaScript packages, which are listed at:

- [Python dependencies](https://github.com/microbiomedata/nmdc-server/blob/main/pyproject.toml)
- [JavaScript dependencies](https://github.com/microbiomedata/nmdc-server/blob/main/web/package.json)

## Architecture

Here's a block diagram depicting the high-level architecture of the NMDC Data Portal.

```mermaid
%% Docs: https://mermaid.js.org/syntax/architecture.html
architecture-beta
    group frontend[Frontend]
    service vue(server)[Vue] in frontend
    service nginx(server)[Nginx] in frontend

    group backend[Backend]
    service postgres(database)[PostgreSQL] in backend
    service zipstreamer(server)[ZipStreamer] in backend
    service fastapi(server)[FastAPI] in backend
    
    service filestorage(cloud)[Data Storage]

    vue:R         -- L:nginx
    nginx:B       -- T:fastapi
    fastapi:R     -- L:zipstreamer
    zipstreamer:R -- L:filestorage
    fastapi:L     -- R:postgres
```

## Development documentation

Here are some resources people can use to learn about the development of the NMDC Data Portal.

- [Developer guide](https://github.com/microbiomedata/nmdc-server/blob/main/docs/development.md)
- [Frontend developer guide](https://github.com/microbiomedata/nmdc-server/blob/main/web/README.md)
