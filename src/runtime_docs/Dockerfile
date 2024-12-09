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
    git sparse-checkout set --no-cone /docs /mkdocs_overrides /mkdocs.yml && \
    git checkout

# Compile source documents into HTML.
RUN cd nmdc-runtime && \
    echo '{\
        "INHERIT": "mkdocs.yml",\
        "site_dir": "/html",\
        "site_url": "http://localhost:8000/"\
    }' | mkdocs build -f -

EXPOSE 8000

# Serve the built documentation.
# Reference: https://docs.python.org/3/library/http.server.html
CMD ["python", "-m", "http.server", "8000", "--bind", "0.0.0.0", "--directory", "/html"]
