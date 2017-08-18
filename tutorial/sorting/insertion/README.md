# InsertionSort

Overview
---
A simple, in-place, comparison-sort algorithm which works by dividing the input
lists into two parts; one sublist of items already sorted and the other sublist 
remaining to be sorted. Originally, one sublist is empty (and thus sorted), 
while the other is the entire (unsorted) list. The algorithm then proceeds 
by finding the smallest (or largest--depending on how you code it) element 
in the unsorted list and swaps it with the leftmost unsorted element; 
moving the sublist boundaries one element to the right.

The primary performance-advantage being that, even when being compared to more 
complicated algorithms: better at dealing with auxiliary memory--like RAM.
This algorithm is terribly inefficient on large lists.

![][1]

Usage
---
`make [--silent] args=T`
`make [--silent] clean`

`javac *.java`
`java SelectionSort T`

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
`make --silent args=../.tests/input.txt`
`make args='3 2 1'`
`make clean`

`python test.py ../.tests/.input.txt`
`python test.py 3 2 1`
`python clean`

Performance
---
* Time: Ω(n^2) | θ(n^2) | O(n^2)
* Space: O(1)

![][2]

###### Sources: [Wikipedia Commons](https://commons.wikimedia.org/wiki/Main_Page)

--------------------------------------------------------------------------------

<!--- this is where the sources go -->
[1]: ./.res/img1.gif
[2]: ./.res/img2.png
