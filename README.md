# commit_analysis

Welcome to `commit_analysis`! With this python package, you can run analysis and view visualizations on your Git Repositories via the command line. Files representing your commit history and data in `.txt` and `.csv` format will be automatically in your repository directory as well as a report file in `.md` format, which you can also view in a static web page via a link given in your interface.

## Installing and Running

In order to install `commit_analysis`, you must clone this repository locally by running the following in your command line:
```
git clone https://github.com/compsys-progtools/commit_analysis
```
After that, go to wherever you cloned this repository and then run the following in your command line:
```
pip install .
```
After that, go to wherever the repository that you want to run analysis and visualizations on is located by running the following in your command line:
```
cd path/to/your/repository
```
After that, just run the following in your command line to generate all files and get the link to the static web page to view:
```
commit_analysis
```

## Contribute

By default, `commit_analysis` only runs the three basic analytics and visualizations, which is the commits over time, commits per author, and commits per file. Feel free to fork this repository and contribute to the `notebook.ipynb` file which actually runs the code in order to change or add more analytics and visualizations. Also feel free to contribute to any other files as well.
