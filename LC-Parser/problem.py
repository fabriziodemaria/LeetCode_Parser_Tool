from lcparser import *
from here import Solution
import pdb

"""
Usage:
1) Paste the code in module here.py
3) Insert "pdb.set_trace()" wherever in your code to enable debugging
4) From the shell: <python problem.py methodname --tree [1,2,3...]>

Note: --tree is optional and you can still use the debugging tool even for
    exercises that don't reqiure tree structures.
"""

def parse_args():
    import argparse
    import itertools
    import sys

    parser = argparse.ArgumentParser(description='Paste your code in this module and start debugging!')
    parser.add_argument('mname', action="store",
                        help='Name of the method called by LeetCode')
    parser.add_argument('--tree', action="store",
                        help='Paste the LeetCode string representing the Tree structure')
    parser.add_argument('--tree1', action="store",
                        help='Paste the LeetCode string representing the Tree structure')
    parser.add_argument('--tree2', action="store",
                        help='Paste the LeetCode string representing the Tree structure')
    args = parser.parse_args()

    if (args.mname is None):
        print "You must enter the method name via --mname"
        exit
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

    method = getattr(Solution, args.mname)

    if args.tree is not None and args.tree1 is None and args.tree2 is None:
        print method(s,t)
        return

    if args.tree is None and args.tree1 is not None and args.tree2 is not None:
        print method(s,t1,t2)
        return

    print "Arguments error"
    return

if __name__ == "__main__":
    main()
