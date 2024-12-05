NMDC Workflows
==============

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
