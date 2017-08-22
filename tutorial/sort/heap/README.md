# HeapSort

Overview
---
Applications/Purpose

###### Advantages
---
N/A

###### Mechanics
---
N/A

![][1]

Usage
---
`make [--silent] args=T`
`make [--silent] clean`

`javac *.java`
`java HeapSort T`

`python test.py T`

Where _T_ is an array of vals or a text file containing vals. Alternatively,
use make _T_ to quickly recompile and run the Java Test classes with args 
and if you so desire, use the latter make-command to remove all class 
files and spruce up the directory. Make sure that if using the former 
method, that _T_ is within quotations. The `--silent` option can be 
used to minimize Makefile output to be only what you allow.

_Note that `make` and `java[c]` commands occur within ./java dir and any 
python commands occur within the ./py dir._


Example
---
<!--- personalize this for HeapSort -->
`make --silent args=../.tests/input.txt`
`make args='3 2 1'`
`make clean`

`python test.py ../.tests/.input.txt`
`python test.py 3 2 1`
`python test.py clean`


Performance
---
* Time: Ω(n log(n)) | θ(n long(n)) | O(n log(n))
* Space: O(1)

![][2]
![][3]

###### Sources: [Wikipedia Commons](https://commons.wikimedia.org/wiki/Main_Page)

--------------------------------------------------------------------------------
[1]: ./.res/img1.gif
[2]: ./.res/img2.gif
[3]: ./.res/img3.svg
