# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Paper Journal Club'
copyright = '2024, Samuel Carter'
author = 'Samuel Carter'
release = '0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['myst_parser']

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx-bootstrap-theme'
# html_theme = 'pydata-sphinx-theme'
# html_theme = 'sphinx-rtd-theme'
'
html_static_path = ['_static']
html_theme_options = {
    'navbar_title': "Paper Journal Club",
    'globaltoc_depth': 2,
    'globaltoc_collapse': True, 
    'globaltoc_includehidden': True,
}
