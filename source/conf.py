# -*- coding: utf-8 -*-
#
# Configuration file for the Sphinx documentation builder.
#
# This file does only contain a selection of the most common options. For a
# full list see the documentation:
# http://www.sphinx-doc.org/en/master/config

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
sys.path.insert(0, os.path.abspath('./modules'))

from sphinx.highlighting import lexers
from datetime import datetime
# import pine_lexer

# -- Project information -----------------------------------------------------

project = u'REST Integrations Docs'
copyright = str(datetime.now().year) + u', TradingView'
author = u''

# The short X.Y version
version = u'1' # Could be referenced from *.rst with |version| macro

# The full version, including alpha/beta/rc tags
release = u'1.0.0' # Could be referenced from *.rst with |release| macro


# -- General configuration ---------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.githubpages',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
source_suffix = ['.rst', '.md']

# The master toctree document.
master_doc = 'index'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = 'en'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_themes/*']

highlight_language = 'ts'

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
import guzzle_sphinx_theme
html_translator_class = 'guzzle_sphinx_theme.HTMLTranslator'
html_theme = 'guzzle_sphinx_theme'

html_theme_path = guzzle_sphinx_theme.html_theme_path()

# Custom sidebar templates, maps document names to template names.
html_sidebars = {
    '**': ['logo-text.html', 'globaltoc.html', 'searchbox.html']
}

html_title = u'REST Integrations Docs'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
html_theme_options = {
    # Set the name of the project to appear in the sidebar
    'project_nav_name': u'REST Integrations FAQ',
}
# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# Custom sidebar templates, must be a dictionary that maps document names
# to template names.
#
# The default sidebars (for documents that don't match any pattern) are
# defined by theme itself.  Builtin themes are using these templates by
# default: ``['localtoc.html', 'relations.html', 'sourcelink.html',
# 'searchbox.html']``.
#
# html_sidebars = {}


# -- Extension configuration -------------------------------------------------

# readthedocs recommends configuring Sphinx to use gettext_uuid as True 
# If True, then RTD creates '# 9f7272de60e648aca7445e7c0cbd450c' these lines in *.pot files
gettext_uuid = False

# readthedocs recommends configuring Sphinx to use gettext_compact as False to generate .pot files.
gettext_compact = False
