# BubbleSort

Overview
---
A simple sorting algorithm that repeatedly steps through the list to be sorted,
compares each pair of adjacent items and swaps them if they are in the wrong
order. It is named for the way smaller or larger elements “bubble” to the
top of the list. This algorithm is impractical for extremely large and
terribly sorted collections. It; however, still can be used decently
for nearly sorted arrays.

The only significant advantage BubbleSort has over other algorithms, even
including QuickSort, but not on InsertionSort, is its ability to detect
whether or not a list is sorted efficiently. Also since the worst case
space-complexity is O(1), it’s best and average are also O(1). For 
this algorithm, space complexity stays the same.

Usage
---
_from within the java dir_
```
make [--silent] args=T
make [--silent] clean
```

[//]: # (alternatively you can use these more cumbersome commands)
```
javac *.java
java BubbleSort T 
```

_from within the py dir_
`python test.py`

Where _T_ is an array of vals or a text file containing vals. Alternatively,
use make _T_ to quickly recompile and run the Java Test classes with args 
and if you so desire, use the latter make-command to remove all class 
files and spruce up the directory. Make sure that if using the former 
method, that _T_ is within quotations. The `--silent` option can be 
used to minimize Makefile output to be only what you allow.

Example
---
`make --silent args=../.tests/case-1.txt`

Note
---
The testing folder is kept hidden as `./.tests` within this dir.

Testing
---
Values can either be tested manually through the internal source file via 
the commandline or through an input text file. Writing a small script to 
export the necessary values to a text file is also a good way to test 
specific and large amounts of values. 

If the tests are specific to the language, then a testing directory will
exist within the language-specific folder, otherwise, a generic testing 
folder will exist in the same dir as the lang-spec ones.

Performance
---
* Time: Ω(n^2) | θ(n^2) | O(n)
* Space: O(1)
