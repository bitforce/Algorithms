# BubbleSort

Overview
---
A simple sorting algorithm that repeatedly steps through the list to be sorted, 
compares each pair of adjacent items and swaps them if they are in the wrong 
order. It is named for the way smaller or larger elements "bubble" to the 
top of the list. This algorithm is impractical for extremely large and
terribly sorted collections. It; however, still can be used decently 
for nearly sorted arrays.

Usage
---
`javac *.java`
`java Test X`

`python test X` 

Where _X_ is an array of vals or a text file containing vals. _Alternatively_, 
use `make X` to quickly recompile and run the Java Test classes.

Note
---
The only significant advantage BubbleSort has over other algorithms, even 
including QuickSort, but not on InsertionSort, is its _ability to detect
whether or not a list is sorted effeciently_. Also since the worst case 
space-complexity is O(1), it's best and average are also O(1). For this 
algorithm, space complexity stays the same.

Testing
---
Values can either be tested manually or via the commandline or through a 
text file. Suggest resources for generating large specific/large test 
files: [Random.org](https://www.random.org/integers/) or writing a 
small script to export the necessary values to a text file. If the 
tests are specific to the language, then a testing directory will 
exists within the language-specific folder, otherwise, a generic 
testing folder will exist in the same dir as the lang-spec ones.

Performance
---
* Space: O(1)
* Time: Ω(n^2) | θ(n^2) | O(n)
