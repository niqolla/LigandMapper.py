import sys, os, subprocess

def run_prank(pdb_file_WITH_DOT_PDB_EXTENSION):

    # From LigandMapper.py
    pdb_file = pdb_file_WITH_DOT_PDB_EXTENSION
    pdb_dir = "predict_" + pdb_file[:-4]

    # Checking if direcotory named the same as the output exists
    if os.path.isdir(pdb_dir):
        print(f"Directory {pdb_dir}/ already exits. Please change it's name or move it to continue.")
        return None

    # Running analysis
    print(f"Analysing {pdb_file} structure...", file=sys.stderr)
    dir_path = os.path.dirname(os.path.realpath(__file__))
    command = [f'{dir_path}/training_data/prank', 'predict', '-f', pdb_file]
    result = subprocess.run(command, capture_output=True, text=True)
    output = result.stdout

    # If the file is taken to a subfolder, 
    # making the neccessary changes
    if '/' in pdb_file:
        pdb_file = pdb_file.split("/")[-1]

    # Removing temp directories
    print("Removing temporary directories", file=sys.stderr)

    # Geting created directory
    dir_line = output.splitlines()[7]
    dir_start = dir_line.find('[') + 1
    dir_end = dir_line.find(']')
    directory_of_prediction = dir_line[dir_start:dir_end]

    # Removing uneccesarry files
    rm_unn = ['rm', f'{directory_of_prediction}/{pdb_file}_residues.csv', 
            f'{directory_of_prediction}/params.txt', 
            f'{directory_of_prediction}/run.log']
    subprocess.run(rm_unn)

    # Moving to current directory
    mv_cmd = ['mv', directory_of_prediction, './']
    subprocess.run(mv_cmd)

    # Removing the test_directory of the main folder
    test_output_dir_loc = directory_of_prediction.find('test_output/') + 12
    test_output_dir = directory_of_prediction[:test_output_dir_loc]
    rm_cmd = ['rm', '-r', test_output_dir]
    subprocess.run(rm_cmd)

    # Returning the full path of the output folder
    output_dir = os.path.abspath(f"./predict_{pdb_file.replace('.pdb','')}/")
    return output_dir