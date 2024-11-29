# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join('alts-core','alts','core')))
sys.path.insert(0, os.path.abspath(os.path.join('alts-modules','alts','modules')))

project = 'ALTS'
copyright = '2024, Benjamin Gors'
author = 'Benjamin Gors'
version = '0.3'
#release = '0.3'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['sphinx.ext.autodoc',
              'sphinx.ext.autosummary',
              'sphinx.ext.napoleon'
              ]

templates_path = ['_templates']
exclude_patterns = ['**/tests/',
                    '.venv/',
                    'testing',
                    'backup']

add_module_names = False
toc_object_entried_show_parents = "hide"
autodoc_default_options = {
    
}
# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "sphinx_book_theme"
html_title = "The Active Learning Test Suite"
html_theme_options = {
    "repository_url": "https://github.com/bela127/alts-core}",
    "use_repository_button": True,
}
"""
"navigation_with_keys" : True,
"sidebarwidth" : 350,
"body_max_width" : "none",
"collapsiblesidebar" : True,
"headbgcolor" : "Aquamarine",
"codebgcolor" : "PaleGoldenRod",
"""
html_static_path = ['_static']
html_css_files = ['css/functions.css']
