# This Dockerfile can be used to build a container image that serves a built version of the Runtime docs.
# To build: $ docker build --progress=plain --no-cache --tag runtime-docs --file Dockerfile .
# To run:   $ docker run --name runtime-docs -p 8000:8000 runtime-docs

# Base this container image upon the official Python container image.
# Reference: https://hub.docker.com/_/python
FROM python:3.12

WORKDIR /src

# Install dependencies of Runtime docs.
RUN python -m pip install --upgrade pip && \
    python -m pip install \
                    mkdocs-material \
                    mkdocs-mermaid2-plugin \
                    mkdocs-jupyter \
                    pymdown-extensions

# Fetch Runtime docs source directory and some supporting files.
#
# Note: Here, I'm using a combination of the technique described in https://stackoverflow.com/a/52269934 (i.e., cloning
#       without checking anything out, then doing a sparse checkout) and a technique described in
#       https://github.blog/open-source/git/get-up-to-speed-with-partial-clone-and-shallow-clone/ (i.e., cloning only a
#       specific branch, and only the latest commit—no deeper—on that branch). By using that combination of techniques,
#       we save time, bandwidth, and disk space.
#
RUN git clone --no-checkout --depth=1 --single-branch --branch=main --filter=tree:0 \
      https://github.com/microbiomedata/nmdc-runtime && \
    cd nmdc-runtime && \
    git sparse-checkout set --no-cone /docs && \
    git checkout

# Copy files we can use to override parts of the Material for MkDocs theme.
COPY mkdocs_overrides/main.html nmdc-runtime/docs/mkdocs_overrides/main.html

# Compile source documents into HTML.
#
# Note: Since passing configuration overrides to `mkdocs` via STDIN (i.e. with the `-f -` option)
#       establishes the current working directory as the reference point from which relative paths
#       defined in `mkdocs.yml` are resolved, we change the working directory to the directory
#       containing the `mkdocs.yml` file. That way, relative paths are once again relative to
#       the `mkdocs.yml` file (which is the norm when not overriding config via STDIN).
#
# References:
# - https://www.mkdocs.org/user-guide/cli/
# - https://www.mkdocs.org/user-guide/configuration/#configuration-inheritance
# - https://squidfunk.github.io/mkdocs-material/setup/changing-the-logo-and-icons/#favicon
# - https://squidfunk.github.io/mkdocs-material/setup/setting-up-the-footer/?h=copyright#copyright-notice
#
RUN cd nmdc-runtime && \
    cd docs && \
    echo '{\
        "INHERIT": "mkdocs.yml",\
        "site_dir": "/html",\
        "site_url": "http://localhost:8000/",\
        "extra": {\
          "analytics": {\
            "provider": "google",\
            "property": "G-VH6HKVLCWN"\
          }\
        }\
    }' | mkdocs build -f -

EXPOSE 8000

# Serve the built documentation.
# Reference: https://docs.python.org/3/library/http.server.html
CMD ["python", "-m", "http.server", "8000", "--bind", "0.0.0.0", "--directory", "/html"]
