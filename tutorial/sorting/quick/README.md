# QuickSort

Overview
---
Applications/purpose

###### Advantages
N/A

###### Mechanics
QuickSort works by selecting an element--can be random; preferably as close to the
middle as possible--to be the pivot element, such that all elements lesser than it 
get swapped onto its left side and all elements grater get moved to the right of 
it. Naturally as the algorithm walks through the array, this creates an inherent 
divide

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
