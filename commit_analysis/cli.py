import click
import os
from .analysis import generate_commit_history, parse_commit_history
from .visualization import generate_plots
from .report import generate_report, convert_md_to_ipynb

@click.command()
def main():
    if not os.path.isdir('.git'):
        click.echo('Error: Current directory is not a git repository.')
        return

    commit_history_txt = 'commit_history.txt'
    commit_data_csv = 'commit_data.csv'
    report_md = 'commit_report.md'
    report_ipynb = 'commit_report.ipynb'

    generate_commit_history(commit_history_txt)
    click.echo('Generated commit_history.txt')

    parse_commit_history(commit_history_txt, commit_data_csv)
    click.echo('Generated commit_data.csv')

    generate_plots(commit_data_csv)
    click.echo('Generated plot images.')

    generate_report(report_md)
    click.echo('Generated commit_report.md')

    convert_md_to_ipynb(report_md, report_ipynb)
    click.echo('Generated commit_report.ipynb')

    click.echo('Analysis complete.')

if __name__ == '__main__':
    main()
