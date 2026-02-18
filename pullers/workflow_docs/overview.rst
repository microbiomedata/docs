:github_url: https://github.com/microbiomedata/docs/blob/main/pullers/workflow_docs/overview.rst

..
   Note: The above `github_url` field is used to force the target of the "Edit on GitHub" link
         to be the specified URL. You can learn more about the field at:
         https://sphinx-rtd-theme.readthedocs.io/en/stable/configuring.html#confval-github_url

NMDC Workflows
==============

General Guidelines
------------------

NMDC aims to integrate existing open-source bioinformatics tools into standardized workflows for processing raw multi-omics data to produce interoperable and reusable annotated data products. Any commercial software are optional alternatives and not required.

Execution Environment
---------------------

Two common ways to install and run the NMDC workflows:

 - Native installation
 - Containers

The NMDC workflows have been written in WDL and require a WDL-capable Workflow Execution Tool (i.e., Cromwell). To ease the native installation, Docker images have been created for the third-party tools for all of the workflows as well. The workflows use the corresponding Docker images to run the required third-party tools. Databases must be downloaded and installed for most of the workflows.
