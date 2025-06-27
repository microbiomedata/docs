# Note: The values in this file were copied from: https://github.com/microbiomedata/workflow_documentation/blob/master/docs/conf.py

# The name of the _documented_ project.
# Docs: https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-project
project = 'NMDC Workflows'

# The author of the _documented_ project.
# Docs: https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-author
author = 'National Microbiome Data Collaborative'

# A copyright statement.
# Docs: https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-copyright
copyright = '2025, National Microbiome Data Collaborative'

# The documented project's _simplified_ and _full_ version identifiers.
# Note: This chained assignment keeps them identical to one another.
# TODO: Do team members expect these to be kept in sync with anything external?
# Docs: https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-version
# Docs: https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-release
version = release = '0.1.0'

# The source document containing the `toctree` for which we want Sphinx to build a document tree.
# Docs: https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-master_doc
master_doc = 'index'

# The theme for HTML output.
# Docs: https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-master_doc
html_theme = 'sphinx_rtd_theme'

# The string you want Sphinx to append to the HTML `<title> tag of each page.
# Docs: https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-html_title
html_title = 'NMDC Workflow Documentation'

# Register paths to directories containing static files.
# Note: This path is relative to the directory containing the `conf.py` file.
# Reference: https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-html_static_path
html_static_path = ['_static']

# The path to the logo we want to use for the documentation website.
# Note: This path is relative to the directory containing the `conf.py` file.
# Reference: https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-html_logo
html_logo = "_static/images/nmdc-logo-bg-white.png"

# Register a custom favicon for the website.
# Reference: https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-html_favicon
html_favicon = '_static/favicon.ico'

# Register a custom JavaScript script for the website to load.
# Note: These paths are relative to the `{html_static_path}` directory.
# Reference: https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-html_js_files
html_js_files = [
    'js/index.js'
]

# Register Sphinx extensions.
# Reference: https://www.sphinx-doc.org/en/master/usage/extensions/index.html
extensions = [
    'sphinx_reredirects',
    'sphinxcontrib.googleanalytics',
]

# -- Sphinx Google Analytics extension --------------------
#
# Reference: https://pypi.org/project/sphinxcontrib-googleanalytics/
#
googleanalytics_id: str = "G-VH6HKVLCWN"
googleanalytics_enabled: bool = True

# -- Sphinx ReRedirects extension ---------------------------
#
# References: 
# - PyPI: https://pypi.org/project/sphinx-reredirects/
# - Docs: https://documatt.com/sphinx-reredirects/usage/
#
# Notes:
# - Link targets are specified relative to the source document.
#
redirects = {
     "chapters/12_Metabolomics/index": "../12_GCMS_Metabolomics/index.html",
     "chapters/13_Natural_Organic_Matter/index": "../14_Natural_Organic_Matter/index.html",
     "chapters/14_Lipidomics/index": "../15_LCMS_Lipidomics/index.html",
}
