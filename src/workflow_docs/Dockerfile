# This Dockerfile can be used to build a container image that serves a built version of the combined workflow docs.
# To build: $ docker build --progress=plain --tag workflow-docs --file Dockerfile .
# To run:   $ docker run --name workflow-docs -p 8000:8000 workflow-docs

# Base this container image upon the official Python container image.
# Reference: https://hub.docker.com/_/python
FROM python:3.10

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
RUN python -m pip install sphinx sphinx_rtd_theme pillow

# Fetch individual workflow docs source directories (i.e. clone the repos in a way that downloads _only_ what we need).
#
# Note: Here, I'm using a combination of the technique described in https://stackoverflow.com/a/52269934 (i.e., cloning
#       without checking anything out, then doing a sparse checkout) and a technique described in
#       https://github.blog/open-source/git/get-up-to-speed-with-partial-clone-and-shallow-clone/ (i.e., cloning only a
#       specific branch, and only the latest commit—no deeper—on that branch). By using that combination of techniques,
#       we save time, bandwidth, and disk space. At the time of this writing, the result occupies less than 10% of the
#       disk space compared to normal clones.
#
RUN mkdir -p /tmp/clones
RUN git clone --no-checkout --depth=1 --single-branch --branch=master --filter=tree:0 https://github.com/microbiomedata/ReadsQC /tmp/clones/ReadsQC                     && cd /tmp/clones/ReadsQC           && git sparse-checkout set --no-cone /docs && git checkout
RUN git clone --no-checkout --depth=1 --single-branch --branch=master --filter=tree:0 https://github.com/microbiomedata/ReadbasedAnalysis /tmp/clones/ReadbasedAnalysis && cd /tmp/clones/ReadbasedAnalysis && git sparse-checkout set --no-cone /docs && git checkout
RUN git clone --no-checkout --depth=1 --single-branch --branch=master --filter=tree:0 https://github.com/microbiomedata/metaAssembly /tmp/clones/metaAssembly           && cd /tmp/clones/metaAssembly      && git sparse-checkout set --no-cone /docs && git checkout
RUN git clone --no-checkout --depth=1 --single-branch --branch=master --filter=tree:0 https://github.com/microbiomedata/mg_annotation /tmp/clones/mg_annotation         && cd /tmp/clones/mg_annotation     && git sparse-checkout set --no-cone /docs && git checkout
RUN git clone --no-checkout --depth=1 --single-branch --branch=master --filter=tree:0 https://github.com/microbiomedata/metaMAGs /tmp/clones/metaMAGs                   && cd /tmp/clones/metaMAGs          && git sparse-checkout set --no-cone /docs && git checkout
RUN git clone --no-checkout --depth=1 --single-branch --branch=main   --filter=tree:0 https://github.com/microbiomedata/metaT /tmp/clones/metaT                         && cd /tmp/clones/metaT             && git sparse-checkout set --no-cone /docs && git checkout
RUN git clone --no-checkout --depth=1 --single-branch --branch=master --filter=tree:0 https://github.com/microbiomedata/metaPro /tmp/clones/metaPro                     && cd /tmp/clones/metaPro           && git sparse-checkout set --no-cone /docs && git checkout
RUN git clone --no-checkout --depth=1 --single-branch --branch=master --filter=tree:0 https://github.com/microbiomedata/metaMS /tmp/clones/metaMS                       && cd /tmp/clones/metaMS            && git sparse-checkout set --no-cone /docs && git checkout
RUN git clone --no-checkout --depth=1 --single-branch --branch=master --filter=tree:0 https://github.com/microbiomedata/enviroMS /tmp/clones/enviroMS                   && cd /tmp/clones/enviroMS          && git sparse-checkout set --no-cone /docs && git checkout

# Rename each "docs" directory to have a chapter number, and move it in preparation for building.
RUN mkdir -p /src/chapters
RUN mv /tmp/clones/ReadsQC/docs           /src/chapters/1_RQC
RUN mv /tmp/clones/ReadbasedAnalysis/docs /src/chapters/2_ReadAnalysis
RUN mv /tmp/clones/metaAssembly/docs      /src/chapters/3_MetaGAssemly
RUN mv /tmp/clones/mg_annotation/docs     /src/chapters/4_MetaGAnnotation
RUN mv /tmp/clones/metaMAGs/docs          /src/chapters/5_MAG
RUN mv /tmp/clones/metaT/docs             /src/chapters/6_MetaT
RUN mv /tmp/clones/metaPro/docs           /src/chapters/7_Metaproteomics
RUN mv /tmp/clones/metaMS/docs            /src/chapters/8_Metabolomics
RUN mv /tmp/clones/enviroMS/docs          /src/chapters/9_NOM

# Upload some local files into the container image.
COPY overview.rst /src/chapters/overview.rst
COPY index.rst    /src/index.rst
COPY conf.py      /src/conf.py

# Compile source documents into HTML.
#
# Note: The `--builder` option is an alias for the `-b` option.
#
# Reference: https://www.sphinx-doc.org/en/master/man/sphinx-build.html
#
RUN sphinx-build --builder html /src /html

EXPOSE 8000

# Serve the built documentation.
# Reference: https://docs.python.org/3/library/http.server.html
CMD ["python", "-m", "http.server", "8000", "--bind", "0.0.0.0", "--directory", "/html"]
