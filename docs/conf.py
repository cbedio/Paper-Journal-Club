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

html_theme = 'sphinx_rtd_theme'

html_static_path = ['_static']

html_css_files = [
    'custom.css',
]


html_theme_options = {
    'navbar_title': "Paper Journal Club",
    'globaltoc_depth': 2,  # Show subheaders in the sidebar across all pages
    'globaltoc_collapse': False,  # Prevent the table of contents from collapsing
    'globaltoc_includehidden': True,  # Ensure all pages are included in the TOC
    'navbar_links': [
        ('Home', 'index'),
        ('Reading List', 'reading_list', [
            ('October 2024', 'reading_list#october'),
            ('November 2024', 'reading_list#november'),
        ]),
    ]
}

# html_theme = 'furo'

# # Optional: Customize theme options
# html_theme_options = {
#     "sidebar_hide_name": True,
#     "light_css_variables": {
#         "color-brand-primary": "#0072B2",
#         "color-brand-content": "#333333",
#     },
#     "default_color_mode": "dark",
#     "source_repository": None,
# }

html_context = {
    "display_github": False,
    "display_source": False,
    "display_bitbucket": False,
    "display_gitlab": False,
}