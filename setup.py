from setuptools import setup, find_packages

setup (
    name = 'commit_analysis',
    version='0.1.0',
    packages = find_packages(),
    install_requires = [
        'Click', 
        'pandas',
        'matplotlib',
        'myst-parser',
        'myst-cli',
        'jupytext',
    ],
    entry_points={
        'console_scripts': [
            'commit_analysis = commit_analysis.cli:main',
        ],
    },
    include_package_data = True,
)
