# Ingesters

## Overview

This directory contains code related to pulling (i.e. ingesting) source files from upstream Git repositories
**and compiling** them into web-based documentation. In that sense, the name "ingesters" doesn't quite account
for everything that's going on here.

In addition to containing code related to ingestion, the `workflow_docs` directory also contains some documentation
content source files, which the workflow documentation ingester combines those content source files with the ones it
pulls from the upstream repositories, to produce a single Sphinx website about workflows. 
