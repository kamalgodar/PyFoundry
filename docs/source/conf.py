# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import os
import sys
import toml

sys.path.insert(0, os.path.abspath("../../"))

def _get_project_meta():
    try:
        pyproject_path = os.path.abspath(
            os.path.join(os.path.dirname(__file__), "../..", "pyproject.toml")
        )
        return toml.load(pyproject_path)["project"]
    except FileNotFoundError:
        raise FileNotFoundError(f"Could not find pyproject.toml at {pyproject_path}")


pkg_meta = _get_project_meta()
project = pkg_meta["name"]
copyright = "2025, Kamal Godar"
author = pkg_meta["authors"][0]["name"]

version = pkg_meta["version"]
release = version

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
]

templates_path = ['_templates']
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
