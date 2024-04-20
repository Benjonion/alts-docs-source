# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join('..','..','code-src')))

project = 'ALTS-Documentation'
copyright = '2024, Benjamin Gors'
author = 'Benjamin Gors'
version = '0.1'
release = '0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['sphinx.ext.autodoc',
              'sphinx.ext.autosummary',
              'sphinx.ext.napoleon'
              ]

templates_path = ['_templates']
exclude_patterns = ['**/tests']


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'classic'
html_theme_options = {
    "navigation_with_keys" : True,
    "sidebarwidth" : 350,
    "body_max_width" : "none",
    "collapsiblesidebar" : True
}
html_static_path = ['_static']
html_css_files = ['css/functions.css']
