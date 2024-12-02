from setuptools import setup

setup (
    name = 'commit_analysis',
    version = '0.1.0',
    py_modules = ['commit_analysis'],
    install_requires = [
        'Click', 
        'pandas',
        'matplotlib',
        'myst-parser',
        'jupytext',
    ],
    entry_points = {
        'console_scripts': [
            'commit_analysis = commit_analysis:main',
        ],
    ),
    include_package_data = True,
)
