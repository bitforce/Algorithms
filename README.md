# Algorithms

Overview
---
A complete library of personally developed and standard algorithms along with 
explanations of their use-cases, performance-analysis, and code-construction.
Languages used: Java & Python; however, there are expectations to expand 
to: C/C++, Ruby, Go, JavaScript, Shell, Haskell, Ocaml, Perl, X86. The 
idea behind this project being the ability to view via many lenses
how languages evolve, differ, and adapt to best fit their design 
limits and purposes such that they cater to the most fundamental 
and advanced intricacies of logic, with the simplicity of not 
necessarily having to go through cumbersome code docs or 
obscure literature to implement, run, and study.

This project contains the following directories...

Usage
---
There are no requirements or dependencies to install, simply go to the aptly 
named directories to search which algorithms you'd like to know about. You 
know you hit the main portion of the algorithm directory when you find a 
README containing information on the algorithm itself, as will as how to 
run it.


Example
---
Assume you'd like to understand and see the original QuickSort algorithm in 
action, and assuming you are in the project folder, you would simply go 
into [./sorting/quick/standard]() and there you will find a README file 
containing information about QuickSort and how to run it in all the 
available languages.

Note
---
Tutorial directories are ones that contain README files explaining details
regarding the algorithm and the executable files that showcase the algo
properties.

The testing folders are kept hidden as `.tests` within their respective 
algorithm directories--where the README is located. Resources used to 
make the README and contribute to the program are kept in a hidden
`.res` folder. 

Unlike the java directory `make clean` operation, `python test.py clean`
has no output and no option to create output.

An in-place algorithm is one that transforms input without using any 
auxiliary memory/datastructure.

Testing
---
Values can either be tested manually through the internal source file via 
the commandline or through an input text file. Writing a small script to 
export the necessary values to a text file is also a good way to test 
specific and large amounts of values. 

If the tests are specific to the language, then a testing directory will
exist within the language-specific folder, otherwise, a generic testing 
folder will exist in the same dir as the lang-spec ones.

Cleaning
---
Perhaps you do not want to clean each tutorial directory individually, 
but remove all unnecessary files and folders within the entire 
Algorithm's project directory; then you can simply run the 
following command: `./clean.sh`

Contributions
---
N/A

License
---
Licensed under the WTFPL - see [LICENSE](./LICENSE) for explicit details.

Author
---
[LinkedIn](https://www.linkedin.com/in/brandonjohnsonxyz/)
[Personal](https://brandonjohnson.life)
[GitHub](https://github.com/bitforce)

##### shameless plugs
BTC : [16euoYuArXAL2y8kqBgofpvRZ2SevjbqME]()
LTC : [LXU7u4LXBaACBJDEAQoBqipjg5LUzpXxbR]()
DSH : [Xg5Xo39xkiL3Uk8FxUfiHDcmGuANFLovnn]()
DCR : [DsS6rEmn2k2kaLvqgFw2gy5kuQnE3X5jy2D]()

(ANT / EOS / ETH / GNO / GNT / REP)
[0xDB4262baD41150ba2db79441D88Eb99d50c0262b]()

_Not that I expect to make any money off this project, but I am curious to 
see what would happen_.
