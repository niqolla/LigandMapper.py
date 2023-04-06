
![alt text](img/logo.png)

# Requirements

OS: Linux or Mac

This is a standalone package, however it requires python3 and java to run. 

### Python3 check:
```
python3 --version
```
Should return something like: 
```
Python 3.x.y
```
(otherwise you will need to install it)

### Java check:
```
java --version
```
Should return something like: 
```
openjdk 11.0.18 2023-01-17
OpenJDK Runtime Environment (build 11.0.18+10-post-Ubuntu-0ubuntu122.04)
OpenJDK 64-Bit Server VM (build 11.0.18+10-post-Ubuntu-0ubuntu122.04, mixed mode, sharing)
```
(otherwise you will need to install it)

# Installation of LignadMapper.py

Once you have python3 and java on your machine, clone the repository or download it on your computer.

Change directory to the folder where you downloaded the zip:

```
cd {folder} 
```

Unzip file and enter folder:

``` 
unzip LigandMapper.py-main.zip

cd LigandMapper.py-main
```

And run:

```
python3 installMe.py 
```

During the installation you will be prompted to enter the password for sudo because the file needs to create a link in the /usr/bin/ folder.

After a successful installation you can remove the zip and the LigandMapper.py-main.zip directory. 

# Commands
Note: The ouput is to the standard error.
```
usage: LigandMapper.py [-h] [-l {file}.pdb] [-o {pdb_name}] [-d {direcory_name}] [--local_many [{file1}.pdb {file2}.pdb ...]] [--online_many [{pdb_name1} {pdb_name2} ...]] [-v] [-ch]
                       [-pm]

LigandMapper.py is a python script build to predict ligand binding sites of proteins from their .pdb files.

optional arguments:
  -h, --help            show this help message and exit
  -l {file}.pdb, --local {file}.pdb
                        One pdb local file.
  -o {pdb_name}, --online {pdb_name}
                        Get a pdb file from the pdb server and analyse that.
  -d {direcory_name}, --directory {direcory_name}
                        Analyse all files located in one local directory.
  --local_many [{file1}.pdb {file2}.pdb ...]
                        Analyse many local pdb files.
  --online_many [{pdb_name1} {pdb_name2} ...]
                        Get many pdb files from the pdb server and analyse them.
  -v, --verbose         Get more detailed output of the process to the standard error.
  -ch, --chimera        Open chimera immediately when file is ready to be visualised. Only applies to local and online SINGLE file.
  -pm, --pymol          Open pymol immediately when file is ready to be visualised. Only applies to local and online SINGLE file.
```

## Examples

#### Local
* If you have one protein structure pdb file (ex. 1gln.pdb) on your computer and you want to predict the ligand binding pockets, run the --local (-l) method:
```
LigandMapper.py -l 1gln.pdb 
```

#### Online
* If you know whats the pdb name but you don't have the pdb file downloaded, you can automatically download it and run the analysis with the --online (-o) method:
```
LigandMapper.py -o 1gln
```

#### Directory
* If you have a directory of pdb files you want to analyse, run the --directory (-d) method:
```
LigandMapper.py -d directory_name/
```
* Or, my advice is, to run this once you have changed into the directory with the files (that way all the output will be stored in the same directory):
```
cd directory_name/
LigandMapper.py -d ./
```

#### Many local
* If you have many local files that you want to analyse, but they're not exclusively gropued in one directory, you can just list them with the --local_many method:
```
LigandMapper.py --local_many 1gln.pdb 2ew2.pdb subfol1/1gln.pdb  
```
#### Many online
* If you want to download from the pdb server and analyse many pdb files, list them with the --online_many method:
```
LigandMapper.py --online_many 1gn3 2ew2 1gln
```

### Visualisation:
* The output can directly visualised with the --chimera (-ch) and --pymol (-pm) switch, given that you have them installed on your computer, by including the switch when running the comand. Note: this only woks for the single-file methods (-l (--local) and -o (--online)); for the --directory, --online_many and --local_many you need to open the visualisation cmd files manually (see: Output below).

Ex. 
```
LigandMapper.py -l 1gln.pdb -ch
LigandMapper.py -o 1gln -pm
```

# Output

A prediction with a file ```{pdb}.pdb``` will create the following structure in the folder in which LigandMapper.py was executed. 

```
predict_{pdb}/
├── {pdb}.pdb_predictions.tsv
└── visualizations/
    ├── chimera_{pdb}.cmd
    ├── {pdb}.pdb.pml
    └── data/
        ├── {pdb}.pdb_points.pdb.gz
        └── {pdb}.pdb 
```