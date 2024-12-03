import subprocess
import pandas as pd

def generate_commit_history(output_file):
    command = [
        'git', 'log',
        '--name-only',
        '--pretty=format:%h , %an , %cd'
    ]
    with open(output_file, 'w') as f:
        subprocess.run(command, stdout = f, text = True)

def parse_commit_history(input_file, output_file):
    with open(input_file, 'r') as chtxt:
        ch_text = chtxt.read()

    chunks = ch_text.strip().split('\n\n')
    ch_data = []

    for chunk in chunks:
        lines = chunk.strip().split('\n')
        
        if len(lines) > 1:
            header_parts = lines[0].split(' , ', maxsplit = 2)
            
            if len(header_parts) == 3:
                commit_hash, author_name, commit_date = header_parts
                file_names = lines[1:]
                
                for file_name in file_names:
                    ch_data.append([commit_hash, author_name, commit_date, file_name.strip()])

    df = pd.DataFrame(ch_data, columns = ['commit_hash', 'author_name', 'commit_date', 'file_name'])

    df['commit_date'] = pd.to_datetime(df['commit_date'], errors = 'coerce', utc = True)
    df = df.dropna(subset = ['commit_date'])
    df['commit_date'] = df['commit_date'].dt.tz_convert('US/Eastern')

    df.to_csv(output_file, index = False)
