# QuickSort

Overview
---
Applications/Purpose

###### Advantages
N/A

###### Mechanics
N/A

###### Code
[A.1](): The `partition()` method takes the last element as the pivot and places the 
pivot element at its correct position in the sorted array, and places elements 
smaller than it to the left of it and all other elements to the right.
[A.2](): A pivot index is created and set as the last element and a current 
index is created and set to the first element.
[A.3](): Index variable `j` is set to the low element and traverses than array and 
if the element at `j` is less than the pivot, then the current index `i` is 
incremented and is swapped with `j` so that an order exists.
[A.4](): The second swap functionality that switches the last and second to last 
element.
[A.5](): The `quickSort()` method is simply a recursive sorting method that takes 
advantage of the `partition()` method using a conditional to check whether the 
values of left (low) partition are actually smaller than the values of the 
right (high) partition. These partitions get naturally put back together 
the recursive returns.
[A.6](): The parameters are check to see if the low variable is actually smaller 
than the high variable, which if so, a partition is created using said variables 
and two recursive sorts are called to then sort each partition into smaller 
pieces and then sort those smaller partitions.

![][1]

Usage
---
`make [--silent] args=T`
`make [--silent] clean`

`javac *.java`
`java QuickSort T`

`python test.py T`

Where _T_ is an array of vals or a text file containing vals. 


Example
---
`make --silent args=../.tests/input.txt`
`make args='3 2 1'`
`make clean`

`python test.py ../.tests/.input.txt`
`python test.py 3 2 1`
`python test.py clean`


Performance
---
* Time: Ω(n log(n)) | θ(n long(n)) | O(n^2)
* Space: O(log(n))

![][2]
![][3]

###### Sources: [Wikipedia Commons](https://commons.wikimedia.org/wiki/Main_Page)

--------------------------------------------------------------------------------
[1]: ./.res/img1.gif
[2]: ./.res/img2.png
[3]: ./.res/img3.gif
