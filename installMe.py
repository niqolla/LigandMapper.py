import platform, subprocess, sys, os

def prompt_manual_install(reason):
    print(reason, "Please follow through the installation manually.", sep='')
    sys.exit(1)


def install():
    env = subprocess.run('env', capture_output=True, text=True).stdout
    path = ''
    for line in env.splitlines():
        if line.startswith('PATH='):
            path = line[5:]
    if path == '':
        prompt_manual_install('No direcotories were found in you $PATH variable. ')
    
    dir_dict = {}
    i = 1 
    
    for dir in list(set(path.split(':'))):
        if dir.endswith('/bin'):
            dir_dict.update({i:dir})
            print(i, ' -- ', dir)
            i+=1

    print("Select a number corrsponding to the directory for installing the application.")
    if '/usr/bin' in dir_dict.values():
        print('Recomended: /usr/bin  Number: ', end='')
        for key,value in dir_dict.items():
            if value=='/usr/bin':
                print(key)

    selected = int(input('Please select a number: '))
    print(selected, dir_dict[selected])

    selected_dir = dir_dict[selected]

    test = subprocess.run(['LigandMapper.py'], shell=True, capture_output=True, text=True, check=False)
    if test.returncode == 0:
        prompt_manual_install('Another package called "LigandMapper.py" already installed.')

    abs_LM = os.path.abspath('LigandMapper/')
    home_dir_hidden = os.path.join(os.path.expanduser('~'),'.LigandMapper' ) 
    print('Copying:', abs_LM, 'to:', home_dir_hidden)
    subprocess.run(['sudo', 'cp', '-r', abs_LM, home_dir_hidden])

    LP_py = os.path.join(home_dir_hidden, 'LigandMapper.py')
    dest_py = os.path.join(selected_dir, 'LigandMapper.py')
    print('Creating a symbolic link from:', LP_py, 'to:', dest_py)
    subprocess.run(['sudo', 'ln', '-s', LP_py, dest_py])

    test = subprocess.run(['LigandMapper.py'], shell=True, capture_output=True, text=True, check=False)
    if test.returncode != 0:
        prompt_manual_install('There was an error with the installation. ')
    print('\nLigandMapper.py sucessfully installed. You can now safetly delete this directory.')
    print('Type LigandMapper.py in the terminal to see the options.')
    

if platform.system() == 'Linux' or platform.system() == 'Darwin':
    install()
else:
    prompt_manual_install("It seems that you don't have Linux or Mac. ")