# QuickSort

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
N/A

###### Advantages
The pivot element and recursive sort implementation makes this algorithm naturally 
nimble and coherent. Unlike standard [sub]array splits, which usually occur in the 
middle, by using the pivot, you can choose where to start the array separation and 
optimize the algorithm by shifting the pivot based on how [un]sorted the array is. 
See the design section below for Quicksort optimization explanations.

###### Mechanics
QuickSort works by selecting an element--can be random; preferably as close to the
middle as possible--to be the pivot element, such that all elements lesser than it 
get swapped onto its left side and all elements grater get moved to the right of 
it. Naturally as the algorithm walks through the array, this creates an inherent 
divide...

###### Analysis
N/A

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
changing structure of the array as it is sorted.

###### Optimizations
To make sure at most O(log n) space is used, recurse first into the smaller side 
of the partition, then use a tail call to recurse into the other. When the 
number of elements is below some threshold (perhaps ten elements), switch 
to a non-recursive sorting algorithm such as insertion sort that performs 
fewer swaps, comparisons or other operations on such small arrays. 

The ideal 'threshold' will vary based on the details of the specific implementation. 

An older variant of the previous optimization: when the number of elements is less than the threshold k, simply stop; then after the whole array has been processed, perform insertion sort on it. Stopping the recursion early leaves the array k-sorted, meaning that each element is at most k positions away from its final sorted position. In this case, insertion sort takes O(kn) time to finish the sort, which is linear if k is a constant.[20][13]:117 Compared to the "many small sorts" optimization, this version may execute fewer instructions, but it makes suboptimal use of the cache memories in modern computers.[

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

###### Sources: [Wikipedia Commons](https://commons.wikimedia.org/wiki/Main_Page)

--------------------------------------------------------------------------------
[a]: ./.res/img1.gif
[b]: ./.res/img2.gif
