# QuickSort

Overview
---
A general-purpose divide and conquer, sorting algorithm which works by utilizing a 
pivot to divide the array into two subarrays consisting of lesser and greater 
elements and then recursively sorting the subarrays.

![][a]

###### Performance
* Time: Ω(n log(n)) | θ(n long(n)) | O(n^2)
* Space: O(log(n))

###### Advantages
The pivot element and recursive sort implementation makes this algorithm naturally 
nimble and coherent. Unlike standard [sub]array splits, which usually occur in the 
middle, by using the pivot, you can choose where to start the array separation and 
optimize the algorithm by shifting the pivot based on how [un]sorted the array is. 
See the _Design_ section for Quicksort optimization explanations. 

###### Mechanics
QuickSort works by selecting an element--can be random; preferably as close to the
middle as possible--to be the pivot element, such that all elements lesser than it 
get swapped onto its left side and all elements grater get moved to the right of 
it. Naturally as the algorithm walks through the array, this creates an inherent 
divide

###### History
Developed in 1959 by Tony Hoare while in the Soviet Union to enhance a machine 
translation project for the National Physical Library. As a part of the 
translation process, he needed to sort the words of Russian sentences 
prior to looking them up in a Russian-English dictionary that was 
already sorted in alphabetical order. After recognizing that his 
first idea: insertion sort; was to slow, he came up with this.

###### Design
The standard algorithm is based off Lomuto's partition scheme; however, there 
are other partition schemes, like the Hoare's OG original scheme. The design 
tweaks target the algo's pivot, but you can also change it to start at the 
beginning, end, middle, or a random element--case-by-case problems will 
determine the most appropriate implementation.

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
