import sys, os
import OnlineMethod

def local(files):

    if len(files) == 4:
        files = files + '.pdb'
    if os.path.isfile(files):
        print(f'File found {files}', file=sys.stderr)
        return files
    else:
        print('File not found!', file=sys.stderr)
        sys.exit(1)

def online(files, verbose):

    if files.endswith(".pdb"):
        files = files[:-4]
    files = files.lower()

    returned = OnlineMethod.check_and_download_pdb_METHOD(files, verbose) 
    if returned == None:
        sys.exit(1)
    return files

def directory(files):

    dir = files
    if not os.path.isdir(dir):
        print(f'{dir} is NOT a directory', file=sys.stderr)
        sys.exit(1)

    files = []
    for file in os.listdir(dir):
        if file.endswith('.pdb'):
            files.append(file)

    print(f'Directory: {os.path.abspath(dir)}', file=sys.stderr)
    if len(files) == 0:
        print(f'There are no pdb files in {dir}. Make sure that the files have a ".pdb" extension.', file=sys.stderr)
        sys.exit(1)
    else:
        print(f'Found files: {files}', file=sys.stderr)
        return files
    
def local_many(files, verbose):

    failed = []
    succeded = []

    for file in files: 

        if len(file) == 4:
            file = file + '.pdb'
        if os.path.isfile(file):
            succeded.append(file)
            if verbose == True:
                print(f'File found {file}', file=sys.stderr)
        else:
            failed.append(file)
            if verbose == True:
                print('File not found!', file=sys.stderr)

    print(f'Files found: {succeded} \
    \nFiles NOT found: {failed}', file=sys.stderr)

    if len(succeded) == 0:
        sys.exit(1)
    else:
        return succeded

def online_many(files, verbose):
    failed = []
    succeded = []

    files = [file.lower() for file in files]
    files = list(set(files))

    for file in files:
        if file.endswith(".pdb"):
            file = file[:-4]

        returned = OnlineMethod.check_and_download_pdb_METHOD(file, verbose) 
        if returned == None:
            failed.append(file)
        else:
            succeded.append(file)

    print(f'Succeded in obtaining: {succeded} \
          \nFaled to get: {failed}', file=sys.stderr)

    if len(succeded) == 0:
        sys.exit(1)
    else:
        return succeded

