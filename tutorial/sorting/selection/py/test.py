from selectionsort import selection_sort
import shutil
import sys
import os


def test():
    args = sys.argv[1:]
    if len(args) == 0:
        sys.exit("\033[91mcommandline args required\033[0m")
    elif len(args) == 1:
        if sys.argv[1] == 'clean':
            clean()
        else:
            f = open(sys.argv[1], 'r')
            numlist = []
            for line in f:
                for i in line.split():
                    if i.isdigit():
                        numlist.append(int(i))
            write('original.txt', numlist)
            selection_sort(numlist)
            write('modified.txt', numlist)
    else:
        print args
        selection_sort(args)
        print args


def write(fname, data):
    with open(fname, 'w') as f:
        for i in data:
            f.write('%d ' % i)
        f.write('\n')


def clean():
    try:
        filelist = [f for f in os.listdir('.')
                    if f.endswith('.pyc') or f.endswith('.txt')]
        for f in filelist:
            os.remove(f)
    except(Exception):
        pass
    try:
        shutil.rmtree('__pycache__')
    except(Exception):
        pass
    try:
        shutil.rmtree('.cache')
    except(Exception):
        pass


if __name__ == '__main__':
    test()
