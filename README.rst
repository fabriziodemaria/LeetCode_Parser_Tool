This tool allows for debugging when trying to solve problems from LeetCode.org. 
During my practising on the website I usually felt the need to execute the code offline and being able to debug it. 
For now, this tool allows to paste the string used by LeetCode to represent tree data structures and generate the tree for you.


Usage (within the problem.py module):
1) Paste the code under Solution(object) line
2) Paste the method called by LeetCode in the corresponding line you find the
    "main" method
3) Insert "pdb.set_trace()" wherever in your code to enable debugging
4) From the shell: <python problem.py --tree [1,2,3...]>

Note: --tree is optional and you can still use the debugging tool even for
    exercises that don't reqiure tree structures.
