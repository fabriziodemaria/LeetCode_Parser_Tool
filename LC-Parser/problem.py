from lcparser import *
import pdb

"""
Usage:
1) Paste the code under Solution(object) line
2) Paste the method called by LeetCode in the corresponding line you find the
    "main" method
3) Insert "pdb.set_trace()" wherever in your code to enable debugging
4) From the shell: <python problem.py --tree [1,2,3...]>

Note: --tree is optional and you can still use the debugging tool even for
    exercises that don't reqiure tree structures.
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    <<!paste your code here!>>

def parse_args():
    import argparse
    import itertools
    import sys

    parser = argparse.ArgumentParser(description='Paste your code in this module and start debugging!')
    parser.add_argument('--tree', action="store",
                        help='Paste the LeetCode string representing the Tree structure')
    parser.add_argument('--tree1', action="store",
                        help='Paste the LeetCode string representing the Tree structure')
    parser.add_argument('--tree2', action="store",
                        help='Paste the LeetCode string representing the Tree structure')
    args = parser.parse_args()

    return args

def main():
    s = Solution()
    args = parse_args()
    if args.tree is not None:
        t = TreeGenerator(args.tree)
    if args.tree1 is not None:
        t1 = TreeGenerator(args.tree1)
    if args.tree2 is not None:
        t2 = TreeGenerator(args.tree2)
    print <<!paste your method name here!>>

if __name__ == "__main__":
    main()
