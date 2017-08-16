from bubble_sort import bubble_sort
import sys


# accept both numerical and [hidden] text file arguments
# clean directory of compiled files
def test():
    array = sys.argv[1:]
    if len(array) == 0:
        sys.exit("\033[91mcommandline args required\033[0m")
    elif len(array) == 1:
        f = open(str.endswith(".txt", ".txt"))
        print f
    else:
        print array
        bubble_sort(array)
        print array


if __name__ == "__main__":
    test()
