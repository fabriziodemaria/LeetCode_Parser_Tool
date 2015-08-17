# -*- coding: utf-8 -*-
import sys
import ast

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def generateTree(list):
    return None

list = ast.literal_eval(sys.argv[1])

if __name__ == '__main__':
    generateTree(list)
