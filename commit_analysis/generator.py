import subprocess
import os
import textwrap

def generate_page(notebook_ipynb, report_md, output_dir):
    convert_notebook_to_markdown(notebook_ipynb, report_md)
    build_jupyter_book(output_dir)

def convert_notebook_to_markdown(notebook_path, markdown_path):
    command = [
        'jupytext',
        '--to',
        'myst',
        notebook_path,
        '-o',
        markdown_path,
    ]
    result = subprocess.run(command, capture_output=True, text=True)
    print(result.stdout)
    print(result.stderr)
    if result.returncode != 0:
        raise RuntimeError(f"Failed to convert notebook to markdown with return code {result.returncode}")

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
          - toctree.missing
    """)
    with open(config_path, 'w') as f:
        f.write(config_content)
        f.flush()  

    toc_path = os.path.join(directory, '_toc.yml')
    toc_content = textwrap.dedent("""
    format: jb-book
    root: report
    """)
    with open(toc_path, 'w') as f:
        f.write(toc_content)
        f.flush()  

    print(f"Config file written to: {config_path}")
    print(f"TOC file written to: {toc_path}")

    command = ['jupyter-book', 'build', directory, '--config', config_path, '--quiet']
    result = subprocess.run(command, capture_output=True, text=True, cwd=directory)
    
    print(result.stdout)
    print(result.stderr)
    
    if result.returncode != 0:
        raise RuntimeError(f"Jupyter Book build failed with return code {result.returncode}")
