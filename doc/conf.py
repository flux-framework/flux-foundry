###############################################################
# Copyright 2021 Lawrence Livermore National Security, LLC
# (c.f. AUTHORS, NOTICE.LLNS, COPYING)
#
# This file is part of the Flux resource manager framework.
# For details, see https://github.com/flux-framework.
#
# SPDX-License-Identifier: LGPL-3.0
###############################################################

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
import os
import sys

# add `manpages` directory to sys.path
import pathlib

sys.path.append(str(pathlib.Path(__file__).absolute().parent))

from manpages import man_pages
import docutils.nodes

# -- Project information -----------------------------------------------------

project = "flux-foundry"
copyright = """Copyright 2014 Lawrence Livermore National Security, LLC and Flux developers.

SPDX-License-Identifier: LGPL-3.0"""

# -- General configuration ---------------------------------------------------

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

master_doc = "index"
source_suffix = ".rst"

extensions = ["sphinx.ext.intersphinx", "sphinx.ext.napoleon", "domainrefs"]

domainrefs = {
    'rfc': {
        'text': 'RFC %s',
        'url': 'https://flux-framework.readthedocs.io/projects/flux-rfc/en/latest/spec_%s.html'
    },
}

# Disable "smartquotes" to avoid things such as turning long-options
#  "--" into en-dash in html output, which won't make much sense for
#  manpages.
smartquotes = False

def man_role(name, rawtext, text, lineno, inliner, options={}, content=[]):
    section = int(name[-1])
    page = None
    for man in man_pages:
        if man[1] == text and man[4] == section:
            page = man[0]
            break
    if page == None:
        page = "man7/flux-undocumented"
        section = 7

    node = docutils.nodes.reference(
        rawsource=rawtext,
        text=f"{text}({section})",
        refuri=f"../{page}.html",
        **options,
    )
    return [node], []


# launch setup
def setup(app):
    for section in [3]:
        app.add_role(f"man{section}", man_role)


napoleon_google_docstring = True

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "sphinx_rtd_theme"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
# html_static_path = ['_static']

# -- Options for Intersphinx -------------------------------------------------

intersphinx_mapping = {
    "rfc": (
        "https://flux-framework.readthedocs.io/projects/flux-rfc/en/latest/",
        None,
    ),
}
