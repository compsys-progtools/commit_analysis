from setuptools import setup, find_packages

# Setup file including name, version, packages, install requirements, entry points, and package data.

setup (
    name = 'commit_analysis',
    version = '0.1.0',
    packages = find_packages(),
    install_requires = [
        'Click',
        'pandas',
        'matplotlib',
        'myst-parser',
        'jupytext',
        'jupyter-book',  
    ],
    entry_points={
        'console_scripts': [
            'commit_analysis = commit_analysis.cli:main',
        ],
    },
    include_package_data = True,
    package_data = {
        'commit_analysis': ['notebook.ipynb'],
    },
)
