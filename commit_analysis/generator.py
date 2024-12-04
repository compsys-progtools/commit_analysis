import subprocess
import os
import textwrap

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
    print(f"Config file written to: {config_path}")

    toc_path = os.path.join(directory, '_toc.yml')
    toc_content = textwrap.dedent("""
    format: jb-book
    root: report
    """)
    with open(toc_path, 'w') as f:
        f.write(toc_content)
        f.flush()
    print(f"TOC file written to: {toc_path}")

    print(f"Running Jupyter Book build in directory: {directory}")
    print(f"Using config file: {config_path}")

    command = ['jupyter-book', 'build', directory, '--config', config_path, '--quiet']
    result = subprocess.run(command, capture_output=True, text=True, cwd=directory)
    print(result.stdout)
    print(result.stderr)
