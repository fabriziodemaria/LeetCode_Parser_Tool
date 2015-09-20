====================================
LeetCode Offline Debugging Tool
====================================

This tool allows for debugging when trying to solve problems from LeetCode.org.
During my practising on the website I usually felt the need to execute the code offline and being able to debug it, so I started this little project.

***************
Functionalities
***************

Languages supported: Python only.

Input supported: For now, this tool can parse the string used by LeetCode to represent tree data structures and generate the tree for you. It supports exercises that adopt a single tree or two trees. It also provide a simple interface to run your code and adopt the produced data structure as input.

***************
Usage
***************
Clone this repo on your computer by either downloading as ZIP or executing the following command on your terminal:

    git clone https://github.com/fabriziodemaria/LeetCode-Tree-Parser.git

Inside the folder *LC-Parser* you can find the Python module called *here.py*. Paste your code from LeetCode to this module exactly as it is.

In order to execute the exercise, navigate your Terminal to *LC-Parser* folder and execute the following command:

    python problem.py <name of the method called by LeetCode> <optional strings representing the input for the exercise>

This should print the solution for your implementation.

***************
Example
***************
For the following exercise: https://leetcode.com/problems/same-tree/
Paste your code in *here.py* and run the following command:

	python problem.py isSameTree --tree1 [1,2] --tree2 [1,2]

You should get *True*. You can get *False* by passing different trees, of course:

	python problem.py isSameTree --tree1 [1,2] --tree2 [1,1,1]

***************
Debug your code
***************
The nice thing about this tool is the ability to easily execute your code offline and debug it.

Just add the following at the very top of the *here.py* module:

    import pdb

To insert a breakpoint in your code simply add the following line in the desired position:

    pdb.set_trace()
