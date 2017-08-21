# Algorithms

Overview
---
A complete library of personally developed and standard algorithms along with 
explanations of their use-cases, performance-analysis, and code-construction.
The idea behind this project being the ability to view via many lenses how 
languages evolve, differ, and adapt to best fit their design limits and 
purposes such that they cater to the most fundamental and advanced 
intricacies of logic, with the simplicity of not necessarily 
having to go through cumbersome code docs or obscure 
literature to implement, run, and study.

Current language implementations
[Python](https://www.python.org/)
[Java](https://www.java.com/en/)

###### Structure 
Within the top-level dir, exists: project license, readme, shell script, and
the tutorial dir containing everything explained in the overview. The readme 
license, and `clean.sh` are pretty self-explanatory; however, within the 
tutorial dir, there is an organization of algorithms based on their type 
and other traits; you know when you are in the actual specific algorithm 
folder, because a README.md file be there and the last two folders in 
the path name will spell out the algorithm's full name; for example: 
_.../sort/quick/_. The current dir will contain the readme and 
folders corresponding to the language that the algorithm was 
written in. Within those folders 3 main files: the algo file 
ending in that folder name's extension, a test file also 
ending in the same extension, and a comment file to 
explain the code fragments of the algo file. Note 
that some of these dirs will contain an extra 
file, such as in the java folders, to assist 
in compilation and/or argument parameters.

The subdirs containing the readme files and code extension name folders shall
be known as _tutorial dirs_ to make this explanation easier. Therefore; the 
tutorial dirs also contain hidden folders: _.alt_, _.res_, and _.tests_ 
which signify: alternative algo implementation, resources, and tests 
respectively. The alt dir may only appear in some tutorial dirs 
which are known to have variant implementations of the algo and 
those dirs will contain subfolders with the name of the variant 
implementation and the contents of those dirs will look just 
like the tutorial dirs. The res and tests folders; however, 
will always be included in every tutorial dir.

Usage
---
There are no requirements or dependencies to install, simply go to the aptly 
named directories to search which algorithms you'd like to know about. You 
know you hit the main portion of the algorithm directory when you find a 
README containing information on the algorithm itself, as will as how to 
run it. In all cases involving compiling Java files using `make`, the 
argument _T_ will always need to be within quotations; for example:
`make args='3 2 1'` or `make args='path/to/test/file'`; however, 
if _T_ is a path, you may remove quotations since there are no 
non-escaped whitespaces within the path to confuse `Make` 
interpreter.

###### Example
Assume you'd like to understand and see the original QuickSort algorithm in 
action, and assuming you are in the project folder, you would simply go 
into ./sorting/quick/ and there you will find a README file containing
information about QuickSort and how to run it in all the available 
languages. Assuming you'd want to run it Java, you would then go 
to the ./java subdirectory and run a test of sorts. Perhaps you 
would like to see the default test; thus, you would run:
`make args=../.tests/input.txt`
`cat original.txt`
`cat modified.txt`
For large inputs, we test using text files and export both the original file 
and the modified file so you can open it up and see the algorithm's effects.

###### Testing
Values can either be tested manually through the internal source file via 
the commandline or through an input text file. Writing a small script to 
export the necessary values to a text file is also a good way to test 
specific and large amounts of values. 

If the tests are specific to the language, then a testing directory will
exist within the language-specific folder, otherwise, a generic testing 
folder will exist in the same dir as the lang-spec ones.

###### Cleaning
Perhaps you do not want to clean each tutorial directory individually, 
but remove all unnecessary files and folders within the entire 
Algorithm's project directory; then you can simply run the 
following command: `./clean.sh`

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

Contributions
---
N/A

License
---
Licensed under the WTFPL - see [LICENSE](./LICENSE) for explicit details.

Version
---
1.0.0

Author
---
[LinkedIn](https://www.linkedin.com/in/brandonjohnsonxyz/)
[Personal](https://brandonjohnson.life)
[GitHub](https://github.com/bitforce)
