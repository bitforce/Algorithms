# CombSort

Overview
---
A simple sorting algorithm that improves on BubbleSort and where the fundamental idea 
is to eliminate turtles (small values near the end of the list) which are the root 
cause of BubbleSort's poor runtime. In BubbleSort, when any of two elements are 
compared, there is a gap between them with a distance of 1 (because BubbleSort 
compares the current and next element); the idea behind CombSort being a gap
can be more than 1. 


![][a]

###### Performance
* Time: Ω(n) - θ(n^2/2^p) - O(n^2)
* Space: O(1)

###### Constraints
!
Degrades down to O(n^2) in case of unnecessary pivot selections and plausible stack 
overflow error in some implementations due to O(n) embedded recursive calls. 
Another disadvantage is the construction of the partitioning algorithm, 
which always seems to an issue in Quicksort's design--so not an easy 
algorithm to sculpt.

###### Advantages
!
The pivot element and recursive sort implementation makes this algorithm naturally 
nimble and coherent. Unlike standard [sub]array splits, which usually occur in the 
middle, by using the pivot, you can choose where to start the array separation and 
optimize the algorithm by shifting the pivot based on how [un]sorted the array is. 
See the design section below for Quicksort optimization explanations. Other great 
benefits, aside from high performance, include easy implementation with caching 
and internal memory management mechanisms. Quicksort's formulation makes it 
amenable to parallelization.

###### Mechanics
It is designed such that for every iteration of the outer loop, the inner loop's 
swap method is designed so that the gap between elements goes down by steps of a 
_shrink factor_. In the algorithm shown here, arbitrary numbers were chosen, but 
do note that the numbers are just mathematical logic to check whether the gap is 
>= 1 which essentially shows how far apart the two elements being observed 
are; a return of 1 means the elements are next to each other.The space 
usage in the algorithm stays the same since the array's size isn't 
being morphed.

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
Developed by Włodzimierz Dobosiewicz in 1980 and later rediscovered by Stephen 
Lacey and Richard Box in 1991.

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
