from quicksort import quicksort
import shutil
import sys
import os


def test():
    args = sys.argv[1:]
    larg = len(args)
    arg1 = ''
    arg2 = ''
    end = '\033[0m'
    red = '\033[91m'
    if larg == 0:
        sys.exit(red + "commandline args required" + end)
    else:
        arg1 = sys.argv[1]
        if(larg == 2):
            arg2 = sys.argv[2]
    if larg == 1:
        if arg1 == 'clean':
            clean(silent=False)
        elif "../.tests/" in arg1:
            try:
                f = open(arg1, 'r')
                numlist = []
                for line in f:
                    for i in line.split():
                        if i.isdigit():
                            numlist.append(int(i))
                write('original.txt', numlist)
                quicksort(numlist)
                write('modified.txt', numlist)
            except(Exception):
                sys.exit(red + "error reading test file" + end)
        else:
            sys.exit(red + 'incorrect arguments' + end)
    elif larg == 2 and arg1 == '--silent' and arg2 == 'clean':
        clean(silent=True)
    elif larg == 2 and arg1 == 'clean' and arg2 == '--silent':
        clean(silent=True)
    else:
        try:
            print args
            quicksort(args)
            print args
        except(Exception):
            sys.exit(red + 'error running manual test inputs' + end)


def write(fname, data):
    with open(fname, 'w') as f:
        for i in data:
            f.write('%d ' % i)
        f.write('\n')


def clean(silent):
    curdir = [f for f in os.listdir('.')]
    bytcode = False
    pycache = False
    hcache = False
    tfiles = False
    rope = False
    for cur in curdir:
        if '.pyc' in cur:
            bytcode = True
        if '__pycache__' in cur:
            pycache = True
        if '.cache' in cur:
            hcache = True
        if 'modified.txt' and 'original.txt' in cur:
            tfiles = True
        if '.ropeproject' in cur:
            rope = True
    if silent:
        if bytcode:
            filelist = [f for f in os.listdir('.') if f.endswith('.pyc')]
            for f in filelist:
                os.remove(f)
        if pycache:
            shutil.rmtree('__pycache__')
        if hcache:
            shutil.rmtree('.cache')
        if rope:
            shutil.rmtree('.ropeproject')
        if tfiles:
            os.remove('original.txt')
            os.remove('modified.txt')
    else:
        if bytcode:
            filelist = [f for f in os.listdir('.') if f.endswith('.pyc')]
            for f in filelist:
                os.remove(f)
                print 'removed ' + f
        if pycache:
            shutil.rmtree('__pycache__')
            print 'removed __pycache__'
        if hcache:
            shutil.rmtree('.cache')
            print 'removed .cache'
        if rope:
            shutil.rmtree('.ropeproject')
            print 'removed .ropeproject'
        if tfiles:
            os.remove('original.txt')
            os.remove('modified.txt')
            print 'removed test output files'


if __name__ == '__main__':
    test()
