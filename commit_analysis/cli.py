import click
import os
import importlib.resources as resources
from .analysis import generate_commit_history, parse_commit_history
from .myst_generator import generate_myst_page

@click.command()
def main():
    if not os.path.isdir('.git'):
        click.echo('Error: Current directory is not a git repository.')
        return

    output_dir = os.getcwd()

    commit_history_txt = os.path.join(output_dir, 'commit_history.txt')
    commit_data_csv = os.path.join(output_dir, 'commit_data.csv')
    report_md = os.path.join(output_dir, 'report.md')

    try:
        with resources.path('commit_analysis', 'notebook.ipynb') as notebook_path:
            notebook_ipynb = str(notebook_path)
            click.echo(f"Using notebook at {notebook_ipynb}")
    except Exception as e:
        click.echo(f"Error locating notebook.ipynb: {e}")
        return

    generate_commit_history(commit_history_txt)
    click.echo('Generated commit_history.txt')

    parse_commit_history(commit_history_txt, commit_data_csv)
    click.echo('Generated commit_data.csv')

    generate_myst_page(notebook_ipynb, report_md, output_dir)
    click.echo(f"Generated MyST page at {report_md}")
    click.echo("Your MyST page is running.")
    click.echo("Press Ctrl+C to stop the server.")

if __name__ == '__main__':
    main()
