# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys

# sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


# -- Project information -----------------------------------------------------

project = 'NMDC Documentation'
copyright = '2024, The NMDC Team'
author = 'The NMDC Team'

# The full version, including alpha/beta/rc tags
release = '0.1'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
   'myst_parser',
   'sphinx_markdown_tables',
   'sphinx_reredirects',
]

# source_suffix = '.rst'
source_suffix = ['.rst', '.md']
# Add any paths that contain templates here, relative to this directory.
# templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'
html_title = 'NMDC'

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']
# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']
# These paths are either relative to html_static_path
# or fully qualified paths (eg. https://...)
html_css_files = [
    'css/custom.css',
]

# The path to the logo we want to use for the documentation website.
# Note: This path is relative to the directory containing the `conf.py` file.
# Reference: https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-html_logo
html_logo = "_static/images/nmdc-logo-bg-white.png"

# Register a custom favicon for the website.
# Reference: https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-html_favicon
html_favicon = "_static/favicon.ico"

# Register a custom JavaScript script for the website to load.
# Note: These paths are relative to the `{html_static_path}` directory.
# Reference: https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-html_js_files
html_js_files = [
    "js/index.js"
]

# -- Redirects ------------------------------------------

# Redirect old schema documentation URLs to the schema documentation
# that is automatically kept in sync with the schema.
# Reference: https://pypi.org/project/sphinx-reredirects/
redirects = {
    "reference/metadata/xylene": "https://w3id.org/nmdc/xylene",  # the latter redirects to: https://microbiomedata.github.io/nmdc-schema/xylene/
    "reference/metadata/*": "https://w3id.org/nmdc/nmdc",
}

# -- Sphinx Read The Docs Theme -------------------------
#
# Configure "Edit on GitHub" links.
# Reference: https://docs.readthedocs.io/en/stable/guides/edit-source-links-sphinx.html#github
html_context = {
    "display_github": True,
    "github_user": "microbiomedata",
    "github_repo": "docs",
    "github_version": "main",
    "conf_py_path": "/content/legacy_home/src/",  # path to directory containing `conf.py` file
}