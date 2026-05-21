# Configuration file for the Sphinx documentation builder.

# -- Path setup --------------------------------------------------------------

import os
import sys

# conf.py is in:
# C:\Users\pwt887\Documents\github\gemact-code\gemact\source
#
# The gemact package is in:
# C:\Users\pwt887\Documents\github\gemact-code\gemact
#
# Therefore we add:
# C:\Users\pwt887\Documents\github\gemact-code
sys.path.insert(0, os.path.abspath("../.."))


# -- Project information -----------------------------------------------------

project = "GEMAct"
copyright = "2022, Gabriele Pittarello, Edoardo Luini, Manfred Marvin Marchione"
author = "Gabriele Pittarello, Edoardo Luini, Manfred Marvin Marchione"

# The full version, including alpha/beta/rc tags
release = "2022"


# -- General configuration ---------------------------------------------------

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.intersphinx",
    "sphinx.ext.ifconfig",
    "sphinx.ext.viewcode",
    "sphinx.ext.githubpages",
    "sphinx.ext.napoleon",
    "sphinx_sitemap",
    "nbsphinx",
    "sphinxcontrib.bibtex",
]

# Autodoc settings
autoclass_content = "both"

autodoc_default_options = {
    "members": True,
    "undoc-members": False,
    "show-inheritance": True,
    "member-order": "bysource",
}

autodoc_member_order = "bysource"
autodoc_typehints = "description"
add_module_names = False

# Napoleon settings: useful if you later use NumPy-style or Google-style docstrings.
# Your current :param: / :type: docstrings are handled by autodoc/docutils.
napoleon_google_docstring = True
napoleon_numpy_docstring = True
napoleon_include_init_with_doc = True
napoleon_use_param = True
napoleon_use_rtype = True

# Bibliography
bibtex_bibfiles = ["refs.bib"]

# Sitemap
sitemap_filename = "sitemap.xml"

templates_path = ["_templates"]

exclude_patterns = [
    "_build",
    "Thumbs.db",
    ".DS_Store",
    "**.ipynb_checkpoints",
]

# Show Python objects such as classes/functions in the page table of contents
toc_object_entries = True
toc_object_entries_show_parents = "hide"
# -- Options for HTML output -------------------------------------------------

html_baseurl = "https://github.com/GEM-analytics/gemact/"
html_theme = "sphinx_book_theme"
html_title = "gemact"
html_logo = "images/GEMActlogo.png"
html_favicon = "images/webtab.png"

html_static_path = ["_static"]

html_theme_options = {
    "home_page_in_toc": True,
    "repository_url": "https://github.com/gpitt71/gemact-code",
    "repository_branch": "main",
    "path_to_docs": "gemact/source",
    "use_repository_button": True,
    "use_edit_page_button": True,
    "show_toc_level": 3,
}

# Required by sphinx-book-theme when use_edit_page_button=True
html_context = {
    "github_user": "gpitt71",
    "github_repo": "gemact-code",
    "github_version": "main",
    "doc_path": "gemact/source",
}