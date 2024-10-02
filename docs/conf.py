# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "xiangting"
copyright = "2024, Apricot S."
author = "Apricot S."
release = "0.1.0"
version = release


# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

import sys
from pathlib import Path

sys.path.insert(0, str(Path("..", "docs").resolve()))

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.intersphinx",
    "sphinx.ext.todo",
    "sphinx.ext.inheritance_diagram",
    "sphinx.ext.autosectionlabel",
    "sphinx.ext.napoleon",
    "sphinx_rtd_theme",
]

autosummary_generate = True
autosummary_imported_members = True
napoleon_google_docstring = True


def skip_member(app, what, name, obj, skip, options):
    exclude_classes = ["FuluMianzi"]
    if name in exclude_classes:
        return True
    return skip


def setup(app):
    app.connect("autodoc-skip-member", skip_member)


templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]
