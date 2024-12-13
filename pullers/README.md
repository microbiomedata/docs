# Pullers

## Overview

This directory contains code related to pulling (i.e. ingesting) source files from upstream Git repositories
**and compiling** them into web-based documentation. In that sense, the name "pullers" doesn't quite account
for everything that's going on here.

In addition to containing code related to pulling, the `workflow_docs` directory also contains some documentation
content source files, directly, which the workflow documentation puller combines with the ones it
pulls from the upstream repositories, to produce a single Sphinx website about workflows. 
