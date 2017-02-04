#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# AlgoBandits documentation build configuration file, created by
# sphinx-quickstart on Thu Jan 19 17:20:57 2017.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.

from __future__ import print_function  # Python 2/3 compatibility !

import sys
import os
sys.path.insert(0, os.path.abspath('.'))

print("Using python, version %s on %s." % (sys.version, sys.platform))


# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
needs_sphinx = '1.5'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'sphinx.ext.mathjax',
    'sphinx.ext.intersphinx',  # http://www.sphinx-doc.org/en/stable/ext/intersphinx.html
    # From https://bitbucket.org/birkenfeld/sphinx-contrib/
    'sphinxcontrib.googleanalytics',
    'sphinxcontrib.autorun',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The recommonmark Sphinx extension adds support for Markdown files
# https://github.com/rtfd/recommonmark (and it works very well)
try:
    from recommonmark.parser import CommonMarkParser
    source_parsers = {
        '.md': CommonMarkParser,  # README.md is the only concerned file
    }
    source_suffix = ['.rst', '.md']
except ImportError:
    print("recommonmark.parser.CommonMarkParser was not found.\nrecommonmark can be installed with 'pip install recommonmark' (from https://github.com/rtfd/recommonmark)")

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = 'AlgoBandits'
copyright = '2016-2017, Lilian Besson'
author = 'Lilian Besson'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = '0.5'
# The full version, including alpha/beta/rc tags.
release = '0.5'

# http://pypi.python.org/pypi/sphinxcontrib-googleanalytics
# https://bitbucket.org/birkenfeld/sphinx-contrib/src/default/googleanalytics/
googleanalytics_id = 'UA-38514290-2'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
html_last_updated_fmt = '%d %b %Y, %Hh:%Mm:%Ss'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = False


autodoc_default_flags = ['members', 'private-members', 'undoc-members', 'special-members']
# Pour trier dans l'ordre du code et non pas par ordre alphabétique
autodoc_member_order = 'bysource'


# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'alabaster'

# on_rtd is whether we are on readthedocs.org, this line of code grabbed from docs.readthedocs.org
on_rtd = os.environ.get('READTHEDOCS', None) == 'True'

if not on_rtd:  # only import and set the theme if we're building docs locally
    # A installer avec 'pip install sphinx_rtd_theme'
    import sphinx_rtd_theme
    html_theme = 'sphinx_rtd_theme'
    html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
# otherwise, readthedocs.org uses their theme by default, so no need to specify it


# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
# html_theme_options = {}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']


# If given, this must be the name of an image file
# (path relative to the configuration directory) that is the logo of the docs.
# It is placed at the top of the sidebar; its width should therefore not exceed 200 pixels. Default: None.
html_logo = 'logo.png'
