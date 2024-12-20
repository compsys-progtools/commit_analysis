import click
import os
from .analysis import generate_commit_history, parse_commit_history
from .generator import generate_page

# Function to get the user's current working directory and join all of the files to generate with said directory as well as call every other function from other files and display output

@click.command()
def main():
    current_dir = os.getcwd()
    commit_history_txt = os.path.join(current_dir, 'commit_history.txt')
    commit_data_csv = os.path.join(current_dir, 'commit_data.csv')
    notebook_ipynb = os.path.join(os.path.dirname(__file__), 'notebook.ipynb')
    report_md = os.path.join(current_dir, 'report.md')

    generate_commit_history(commit_history_txt)
    print("Generated commit_history.txt")
    parse_commit_history(commit_history_txt, commit_data_csv)
    print("Generated commit_data.csv")

    generate_page(notebook_ipynb, report_md, current_dir)
    print("Generated report.md")
    print("Generate page to view commit analysis")
