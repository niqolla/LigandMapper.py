# download file from PDB database

import sys, os, subprocess
import requests

def getPDBfile(pdb_download, verbose):
    if verbose == True:
        print(f"Requesting PDB entry: {pdb_download}", file=sys.stderr)
    url = f"https://files.rcsb.org/download/{pdb_download}.pdb"
    filename = f"{pdb_download}.pdb"
    response = requests.get(url)

    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.exceptions.HTTPError as e:
        if e.response.status_code == 404:
            print(f"Entry {pdb_download} not found - NOT downloaded.", file=sys.stderr)
        else:
            print("Error:", e, file=sys.stderr)
        return None
    else:
        if os.path.isfile(f'{pdb_download}.pdb'):
            print(f'Same file ({pdb_download}.pdb) is already found in current directory. Overwriting!', file=sys.stderr)
            subprocess.run(['rm', f'{pdb_download}.pdb'])
        else:
            print(f"Entry found. Saving as file {pdb_download}.pdb", file=sys.stderr)
        with open(filename, "wb") as f:
            f.write(response.content)
            print(f"File saved successfully as {pdb_download}.pdb in the current directory\n", file=sys.stderr)
        return 1

