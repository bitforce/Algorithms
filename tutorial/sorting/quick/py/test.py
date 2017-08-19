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
    if larg == 2 and arg1 == '--silent' and arg2 == 'clean':
        clean(silent=True)
    if larg == 2 and arg1 == 'clean' and arg2 == '--silent':
        clean(silent=True)
    try:
        print args
        quicksort(args)
        print args
    except(Exception):
        sys.exit(red + 'arguments not recognized' + end)


def write(fname, data):
    with open(fname, 'w') as f:
        for i in data:
            f.write('%d ' % i)
        f.write('\n')


def clean(silent):
    if silent:
        try:
            filelist = [f for f in os.listdir('.') if f.endswith('.pyc')]
            for f in filelist:
                os.remove(f)
        except(Exception):
            pass
        try:
            os.remove('original.txt')
            os.remove('modified.txt')
        except(Exception):
            pass
        try:
            shutil.rmtree('__pycache__')
        except(Exception):
            pass
        try:
            shutil.rmtree('.ropeproject')
        except(Exception):
            pass
        try:
            shutil.rmtree('.cache')
        except(Exception):
            pass
    else:
        try:
            filelist = [f for f in os.listdir('.') if f.endswith('.pyc')]
            for f in filelist:
                os.remove(f)
                print 'removed ' + f
        except(Exception):
            print 'no byte code files to delete'
        try:
            os.remove('original.txt')
            os.remove('modified.txt')
            print 'removed test output files'
        except(Exception):
            print 'no test output to delete'
        try:
            shutil.rmtree('__pycache__')
            print 'removed __pycache__'
        except(Exception):
            print 'no __pycache__ to delete'
        try:
            shutil.rmtree('.ropeproject')
            print 'removed ropeproject'
        except(Exception):
            print 'no ropeproject to delete'
        try:
            shutil.rmtree('.cache')
            print 'removed cache directory'
        except(Exception):
            print 'no .cache directory to delete'
    sys.exit()


if __name__ == '__main__':
    test()
