import subprocess
import os

def generate_myst_page(notebook_ipynb, report_md, output_dir):
    convert_notebook_to_markdown(notebook_ipynb, report_md)
    start_myst_server(output_dir)

def convert_notebook_to_markdown(notebook_path, markdown_path):
    command = ['jupytext', '--to', 'markdown', notebook_path, '-o', markdown_path]
    subprocess.run(command, check = True)

def start_myst_server(directory):
    command = ['python', '-m', 'myst_cli', 'start']
    subprocess.run(command, cwd = directory)
