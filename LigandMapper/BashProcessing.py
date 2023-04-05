# This file processes the input from the command line

import argparse
import sys

def bash_proccesing():

    parser = argparse.ArgumentParser(prog="LigandMapper.py",
                                     description="""LigandMapper.py is a python script build to predict ligand binding 
                                     sites of proteins from their .pdb files.""")

    parser.add_argument('-l', '--local', metavar='{file}.pdb', help='One pdb local file.')
    parser.add_argument('-o', '--online', metavar='{pdb_name}', help='Get a pdb file from the pdb server and analyse that.')
    parser.add_argument('-d', '--directory', metavar='{direcory_name}', help='Analyse all files located in one local directory.')
    parser.add_argument('--local_many', nargs='*', metavar='{file1}.pdb {file2}.pdb', help='Analyse many local pdb files.')
    parser.add_argument('--online_many', nargs='*', metavar='{pdb_name1} {pdb_name2}', help='Get many pdb files from the pdb server and analyse them.')
    parser.add_argument('-v', '--verbose', action='store_true', help='Get more detailed output of the process to the standard error.')
    parser.add_argument('-ch', '--chimera', action='store_true', help='Open chimera immediately when file is ready to be visualised. Only applies to local and online SINGLE file.')
    parser.add_argument('-pm', '--pymol', action='store_true', help='Open pymol immediately when file is ready to be visualised. Only applies to local and online SINGLE file.')

    args = parser.parse_args()

    LOCAL, ONLINE, DIRECTORY = args.local, args.online, args.directory
    LOCAL_MANY, ONLINE_MANY = args.local_many, args.online_many

    methods_chosen = 0
    method = ''
    files = ''

    arg_list = [LOCAL, ONLINE, DIRECTORY, LOCAL_MANY, ONLINE_MANY]
    arg_list_str = ['LOCAL', 'ONLINE', 'DIRECTORY', 'LOCAL_MANY', 'ONLINE_MANY']


    for i,arg in enumerate(arg_list):
        if arg != None:
            methods_chosen +=1
            method = arg_list_str[i]
            files = arg_list[i]

    if methods_chosen == 1:
        if args.verbose == True:
            print(f'Selected method: {method.lower()}\
                \nSelected file(s): {files}\n', file=sys.stderr)
        return(method, files, args.verbose, args.chimera, args.pymol)   
    elif methods_chosen == 0:
        parser.print_help()
        print("""\nExamples:\n
        LigandMapper.py -l 1gln.pdb
        LigandMapper.py -o 1gln
        LigandMapper.py -d directory_name/
        LigandMapper.py --local_many 1gln.pdb 2ew2.pdb subfol1/1gln.pdb  
        LigandMapper.py --online_many 1gn3 2ew2 1gln
        """, file=sys.stderr)
        sys.exit(0)
    elif methods_chosen > 1:
        print("""\nError! Please choose ONLY ONE method! Examples:
        LigandMapper.py -l 1gn3.pdb
        LigandMapper.py -o 1gn3
        LigandMapper.py -d directory_name/
        LigandMapper.py --local_many 1gn3.pdb 2ew2.pdb subfol1/1gln.pdb  
        LigandMapper.py --online_many 1gn3 2ew2 1gln
        """, file=sys.stderr)
        sys.exit(1)


