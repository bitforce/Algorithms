# CombSort

Overview
---
A general-purpose divide and conquer, sorting algorithm which works by utilizing a 
pivot to divide the array into two subarrays consisting of lesser and greater 
elements and then recursively sorting the subarrays.

![][a]

###### Performance
* Time: Ω(n log(n)) - θ(n long(n)) - O(n^2)
* Space: O(log(n))

###### Constraints
Degrades down to O(n^2) in case of unnecessary pivot selections and plausible stack 
overflow error in some implementations due to O(n) embedded recursive calls. 
Another disadvantage is the construction of the partitioning algorithm, 
which always seems to an issue in Quicksort's design--so not an easy 
algorithm to sculpt.

###### Advantages
The pivot element and recursive sort implementation makes this algorithm naturally 
nimble and coherent. Unlike standard [sub]array splits, which usually occur in the 
middle, by using the pivot, you can choose where to start the array separation and 
optimize the algorithm by shifting the pivot based on how [un]sorted the array is. 
See the design section below for Quicksort optimization explanations. Other great 
benefits, aside from high performance, include easy implementation with caching 
and internal memory management mechanisms. Quicksort's formulation makes it 
amenable to parallelization.

###### Mechanics
QuickSort works by selecting an element somewhere in the array; the location of 
the pivot (front, middle, back, random) implementation is usually based on the 
problem algo is trying to solve. Once the pivot is selected, is begins to part 
the array and swap lesser-value elements in front of it and greater-value 
elements in front of it. Thereafter, it shifts the pivot; again depending 
on the implementation, the pivot is either simply moved over or exactly 
pointed to a specific position in the array. Then the process repeats 
itself recursively until the pivot element reaches the original 
position or it realizes that it need not traverse the array any 
longer. 


One confusing aspect about the pivot, is its traversal. Even though the pivot's 
location is set at one element, the comparison operation doesn't stop there; 
two elements still may be compared before or after the pivot--again, this 
depends on the implementation.

###### Analysis
_BCT_:
  When the partition divides the list into two (nearly) equal pieces, the 
  recursive calls process only half the list size and consequently this 
  makes only n=2^x calls before we reach a list length of 1. As the 
  sublist progressively cuts itself in half, the traversal of said 
  list is on length of that sublist; whereby in an ideal scenario, 
  the list and following sublists split in half perfectly for 
  every partition call.


_WCT_:
  This occurs when the pivot either divides the array into sublists of length 0 
  and n-1 or when the pivot attempts to divide an array where all elements
  equal. The former signifies that the pivot (likely) happened to be the 
  smallest or largest element in the list and the latter proves that you 
  don't know what an algorithm actually is. When this occurs, each 
  recursive call processes a sublist only whose length is only 1 
  less and thus you are making n calls on an array of n length.

  See [figure](./.res/fig1.png) for graphical representation.

_WCS_:
  Space complexity may differ in Quicksort variants; however, for the one found 
  here, it uses in-place partitioning, which only takes O(1) space, but post
  partition, the sublists are recursively sorted; the sublist with the lesser 
  elements being sorted first and requiring at most O(log(n)) space; followed 
  by the other part being sorted using tail recursion or iteration, which 
  doesn't add to the call stack, thus leaving us with O(log(n)) as worst.

###### History
Developed in 1959 by Tony Hoare while in the Soviet Union to enhance a machine 
translation project for the National Physical Library. As a part of the 
translation process, he needed to sort the words of Russian sentences 
prior to looking them up in a Russian-English dictionary that was 
already sorted in alphabetical order. After recognizing that his 
first idea: insertion sort; was to slow, he came up with this.

###### Design
Most standard implementations are based off Lomuto's partition scheme; however, 
there are other partition schemes, like Hoare's _OG_ original scheme. Most of 
these alterations are formed on shifting the pivot [behavior], either by 
simply making it start at the beginning, middle, end, or random element 
and/or by changing the actions of the pivot to more aptly adapt to the 
changing structure of the array as it is sorted. Note the partition 
steps and pivot selection can be done in several different ways and 
are the core design/performance factors.

Some design optimizations include assuring at most O(log n) space is used, 
recurse first into the smaller side of the partition, then use a tail call 
to recurse into the other. When the number of elements is below some 
threshold; perhaps ten elements, switch to a non-recursive sorting 
algorithm such as insertion sort that performs fewer swaps, 
comparisons or other operations on such small arrays.

### Usage

`make [--silent] args=T`
`make [--silent] clean`

`javac *.java`
`java QuickSort T`

`python test.py T`

Where _T_ is an array of vals or a text file containing vals. 


### Example
`make --silent args=../.tests/input.txt`
`make args='3 2 1'`
`make clean`

`python test.py ../.tests/.input.txt`
`python test.py 3 2 1`
`python test.py clean`

![][b]

### Sources

###### Informational
[Wikipedia](https://en.wikipedia.org/wiki/Quicksort)
[YouTube](https://youtu.be/XE4VP_8Y0BU)
[YouTube](https://youtu.be/SLauY6PpjW4)
[Quora](http://qr.ae/TbcAbE)

###### Graphical
[Image 1](https://commons.wikimedia.org/wiki/File:Sorting_quicksort_anim.gif)
[Image 2](https://commons.wikimedia.org/wiki/File:Quicksort-example.gif)
[Image 3](http://users.informatik.uni-halle.de/~jopsi/dssea/chap6.shtml)

--------------------------------------------------------------------------------
[a]: ./.res/img1.gif
[b]: ./.res/img2.gif
