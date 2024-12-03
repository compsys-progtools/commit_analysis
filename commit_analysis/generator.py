import subprocess
import os

def generate_page(notebook_ipynb, report_md, output_dir):
    convert_notebook_to_markdown(notebook_ipynb, report_md)
    build_jupyter_book(output_dir)

def convert_notebook_to_markdown(notebook_path, markdown_path):
    command = [
        'jupytext',
        '--to',
        'markdown',
        notebook_path,
        '-o',
        markdown_path,
    ]
    subprocess.run(command, check = True)

def build_jupyter_book(directory):
    config_path = os.path.join(directory, '_config.yml')
    
    if not os.path.exists(config_path):
        with open(config_path, 'w') as f:
            f.write("title: Commit Analysis Report\n")

    toc_path = os.path.join(directory, '_toc.yml')
    
    with open(toc_path, 'w') as f:
        f.write("format: jb-book\nroot: report\n")

    command = ['jupyter-book', 'build', directory]
    subprocess.run(command, check = True)
