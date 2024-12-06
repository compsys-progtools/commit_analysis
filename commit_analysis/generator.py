import subprocess
import os
import textwrap

# Function to call the other 2 functions in the file

def generate_page(notebook_ipynb, report_md, output_dir):
    convert_notebook_to_markdown(notebook_ipynb, report_md)
    build_jupyter_book(output_dir)

# Function that converts my Colab notebook code into MyST markdown format so that it can be built into a static page via JupyterBook using a subprocess bash command with JupyText

def convert_notebook_to_markdown(notebook_path, markdown_path):
    command = [
        'jupytext',
        '--to',
        'myst',
        notebook_path,
        '-o',
        markdown_path,
    ]
    subprocess.run(command, check = True)

# Function that builds the JupyterBook page by generating the _config.yml and _toc.yml files and runs a subprocess bash command

def build_jupyter_book(directory):
    config_path = os.path.join(directory, '_config.yml')
    config_content = textwrap.dedent("""
    title: Commit Analysis Report
    execute:
      execute_notebooks: force
    sphinx:
      config:
        suppress_warnings:
          - myst.header
          - myst.xref_missing
          - etoc.tableofcontents
    """)
    
    with open(config_path, 'w') as f:
        f.write(config_content)

    toc_path = os.path.join(directory, '_toc.yml')
    toc_content = textwrap.dedent("""
    format: jb-book
    root: report
    """)
    
    with open(toc_path, 'w') as f:
        f.write(toc_content)

    command = ['jupyter-book', 'build', directory, '--quiet']
    subprocess.run(command, check = True)
