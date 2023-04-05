#!/usr/bin/env python3

import sys, subprocess
import BashProcessing, LMFunctions, PrankScript, CreatePDBCMDandSetTypes, CreateTSVFile

method, files, verbose, chimera, pymol = BashProcessing.bash_proccesing()

def open_chimera_pymol(output_dir, file, chimera, pymol):
    if chimera == True:
        ch_out = subprocess.run(['which', 'chimera'], capture_output=True, text=True)
        ch_out = len(ch_out.stdout)
        if ch_out == 0:
            print("It doesn't seem that you have chimera installed.")
            chimera = False
        else: 
            pdb = file[:-4]
            subprocess.run(['chimera', f'{output_dir}/visualizations/chimera_{pdb}.cmd'])
    if pymol == True:
        py_out = subprocess.run(['which', 'pymol'], capture_output=True, text=True)
        py_out = len(py_out.stdout)
        if py_out == 0:
            print("It doesn't seem that you have pymol installed.")
            pymol = False
        else: 
            subprocess.run(['pymol', f'{output_dir}/visualizations/{file}.pml'])

def process_one_file(file_with_DOT_PDB, chimera, pymol):
    file = file_with_DOT_PDB
    output_dir = PrankScript.run_prank(file)
    if output_dir == None:
        return None
    predictions_csv_path, out_dir, pdb, list_of_pocket_objects = CreatePDBCMDandSetTypes.create_pdb_cmd_file_and_set_residue_types(output_dir, file)
    if len(list_of_pocket_objects) == 0:
        print('NO POCKET WERE PREDICTED, REMOVING ADDITIONAL FILES.', file=sys.stderr)
        subprocess.run(['rm', '-r', output_dir])
    else:
        CreateTSVFile.create_tsv_file(predictions_csv_path, out_dir, pdb, list_of_pocket_objects)
        print(f"Output stored in: {output_dir}", file=sys.stderr)
        if chimera == True or pymol == True:
            open_chimera_pymol(output_dir, file, chimera, pymol)

if method == 'LOCAL':
    files_to_go = LMFunctions.local(files)                  # returned file has .pdb
    process_one_file(files_to_go, chimera, pymol)

if method == 'ONLINE':
    files_to_go = LMFunctions.online(files, verbose)        # returned file does NOT have .pdb
    files_to_go += '.pdb'
    process_one_file(files_to_go, chimera, pymol)

if method == 'DIRECTORY':
    files_to_go = LMFunctions.directory(files)              # returns a list of files with .pdb
    for file in files_to_go:
        process_one_file(file, chimera=False, pymol=False)

if method == 'LOCAL_MANY':
    files_to_go = LMFunctions.local_many(files, verbose)    # returns a list of files with .pdb
    for file in files_to_go:
        process_one_file(file, chimera=False, pymol=False)

if method == 'ONLINE_MANY':
    files_to_go = LMFunctions.online_many(files, verbose)   # returns a list of files that do NOT have .pdb
    for file in files_to_go:
        file += '.pdb'
        process_one_file(file, chimera=False, pymol=False)

