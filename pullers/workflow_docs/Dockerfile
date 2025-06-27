# This Dockerfile can be used to build a container image that serves a built version of the combined workflow docs.
# To build: $ docker build --progress=plain --no-cache --tag workflow-docs --file Dockerfile .
# To run:   $ docker run --name workflow-docs -p 8000:8000 workflow-docs

# Base this container image upon the official Python container image.
# Reference: https://hub.docker.com/_/python
FROM python:3.12

WORKDIR /src

# Install dependencies of workflow docs.
#
# Note: The only reason I install `pillow` is that, when it's not installed, the Sphinx build process complains with:
#       ```
#       Cannot scale image! Could not get size from {some SVG image}: Requires Python Imaging Library. [docutils]
#       ```
#       However, even with `pillow` installed, the Sphinx build process still complains in a similar way (although
#       it no longer says "Requires Python Imaging Library").
#
RUN python -m pip install --upgrade pip
RUN python -m pip install \
    sphinx \
    sphinx_rtd_theme \
    pillow \
    sphinx-reredirects==1.0.0 \
    sphinxcontrib-googleanalytics==0.4

# Fetch individual workflow docs sources and arrange them into chapters.
#
# Note: The source files for the overview chapter and Chapter 1 reside
#       in this `docs` repo. We will process those in a subsequent step.
#
COPY fetch_docs_sources.sh /tmp/fetch_docs_sources.sh
RUN chmod +x /tmp/fetch_docs_sources.sh
RUN /tmp/fetch_docs_sources.sh

# Introduce additional source documents and a configuration file.
# Note: The above shell script will have created `/tmp/book/src/chapters/`.
COPY metagenome_workflow_overview/docs /tmp/book/src/chapters/1_Metagenome_Workflow_Overview
COPY _static                           /tmp/book/src/_static
COPY overview.rst                      /tmp/book/src/chapters/overview.rst
COPY index.rst                         /tmp/book/src/index.rst
COPY conf.py                           /tmp/book/src/conf.py

# Compile source documents into HTML.
#
# Notes:
# - This operation is configured via the `/src/conf.py` file.
# - The `--builder` option is an alias for the `-b` option.
#
# Reference: https://www.sphinx-doc.org/en/master/man/sphinx-build.html
#
RUN sphinx-build --builder html /tmp/book/src /html

EXPOSE 8000

# Serve the built documentation.
# Reference: https://docs.python.org/3/library/http.server.html
CMD ["python", "-m", "http.server", "8000", "--bind", "0.0.0.0", "--directory", "/html"]
