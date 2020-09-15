import sys, os
print(os.getcwd())

def make_dir():
    for i in range(1, 10):
        path = os.path.join(os.getcwd(), f'dir_{i}')
        os.mkdir(path)

def del_dir():
    for i in range(1, 10):
        path = os.path.join(os.getcwd(), f'dir_{i}')
        os.rmdir(path)




