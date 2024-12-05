..
    Note: This file was copied from: https://github.com/microbiomedata/workflow_documentation/blob/master/docs/chapters/overview.rst
    TODO: Fix the typo in "Evironment" below (change to "Environment").

Overview
==================

NMDC
----
The National Microbiome Data Collaborative (NMDC) is a new initiative, launched in July 2019 and funded by the Department of Energy’s (DOE) Office of Science, Biological and Environmental Research program, that aims to empower the research community to more effectively harness microbiome data. The NMDC is building an open-source, integrated data science ecosystem aimed at leveraging existing efforts in the microbiome research space, including data standards, quality, integration, and access, to create a linked data discovery portal. Read the `Nature Reviews Microbiology Comment <https://www.nature.com/articles/s41579-020-0377-0>`_ on the NMDC or visit the `NMDC website <https://microbiomedata.org/>`_.

Four national laboratories are working together to produce the NMDC:

 - Lawrence Berkeley National Laboratory
 - Los Alamos National Laboratory
 - Oak Ridge National Laboratory
 - Pacific Northwest National Laboratory


NMDC Workflows
--------------

General Guidelines
--------------------

NMDC aims to integrate existing open-source bioinformatics tools into standardized workflows for processing raw multi-omics data to produce interoperable and reusable annotated data products. Any commercial software are optional alternatives and not required.

Execution Evironment
--------------------

Two common ways to install and run the NMDC workflows:

 - Native installation
 - Containers

The NMDC workflows have been written in WDL and require a WDL-capable Workflow Execution Tool (i.e., Cromwell). To ease the native installation, Docker images have been created for the third-party tools for all of the workflows as well. The workflows use the corresponding Docker images to run the required third-party tools. Databases must be downloaded and installed for most of the workflows.


The NMDC workflows are also available as a web application called `NMDC EDGE <https://nmdc-edge.org/home>`_ . The application has only the NMDC workflows integrated into an updated framework for `EDGE Bioinformatics <https://edgebioinformatics.org/>`_ ; this provides the workflows, third-party software, and requisite databases within a platform with a user-friendly interface. NMDC EDGE is provided as a web application especially for users who are not comfortable with running command line tools or without the computational resources to run the command line/ Docker versions.
