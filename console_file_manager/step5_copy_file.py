import os
import shutil

def copy_file(name, new_name):
    if os.path.isdir(name):
        try:
            shutil.copytree(name, new_name)
        except FileExistsError:
            print('Folder exists')
    else:
        shutil.copy(name, new_name)
