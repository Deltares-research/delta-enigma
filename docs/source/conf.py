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
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'Delta Enigma'
copyright = '2024, Jelle van Miltenburg'
author = 'Jelle van Miltenburg'

# The full version, including alpha/beta/rc tags
release = '0.1'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',  # Auto-generate documentation from docstrings
    'sphinx.ext.napoleon',  # Support for NumPy and Google style docstrings
    'sphinx.ext.viewcode',  # Add links to source code
    #'sphinx_book_theme',
    'myst_parser'            # Add text parser
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------

html_title = "Delta Enigma Data Management Handbook"

# Add logo configuration
html_logo = "_static/logo_Delta-ENIGMA.png"

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_book_theme'


# Add some additional configuration options:
html_theme_options = {
    "repository_url": "https://github.com/Deltares-research/delta-enigma.git",
    "use_repository_button": True,
    "use_fullscreen_button": False,
    "use_download_button": True,
    "collapse_navigation": True,
    "navigation_with_keys": False,
    "show_toc_level": 1,
    "logo_only": True,  # Show only logo in the sidebar
    "home_page_in_toc": True,  # Include home page in navigation
} 

# Add acceptable suffixes 
source_suffix = {
    '.rst': 'restructuredtext',
    '.txt': 'markdown',
    '.md': 'markdown',
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

html_css_files = [
    'custom.css',
]

# Add MyST extensions
myst_enable_extensions = [
    "colon_fence",
    "deflist"
]