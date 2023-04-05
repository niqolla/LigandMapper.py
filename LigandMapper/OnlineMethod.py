import re, sys
import GetPDB

# check if the entry is 4 letters
def is_pdb_entry_name(name):
    pattern = re.compile(r'^[1-6][A-Za-z0-9]{3}$')
    return bool(pattern.match(name))

def check_and_download_pdb_METHOD(files, verbose):
    if is_pdb_entry_name(files) == False:
        print(f"The supplied pdb name ({files}) is not valid. \
              \nPDB entry names consist of four alphanumeric characters, where the first character is a number and the following three characters are alphanumeric.\n", file=sys.stderr)
        return None
    
    get = GetPDB.getPDBfile(files, verbose)
    if get == None:
        return None
    return 1
