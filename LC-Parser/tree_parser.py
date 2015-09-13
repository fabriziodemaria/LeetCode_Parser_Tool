# -*- coding: utf-8 -*-
import sys
import ast
from collections import deque

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def TreeGenerator(string):

    #Handle edge cases
    if string is None or string == "[]":
        return None

    s = string
    list = s[1:-1].split(',')
    head = TreeNode(int(list[0]))
    current = head
    q = deque([])
    i = 0
    while i < len(list):
        if i*2+1 < len(list):
            if list[i*2+1]=="#":
                current.left = None
            else:
                current.left = TreeNode(int(list[i*2+1]))
                q.append(current.left)
        if i*2+2 < len(list):
            if list[i*2+2]=="#":
                current.rightt = None
            else:
                current.right = TreeNode(int(list[i*2+2]))
                q.append(current.right)
        i=i+1
        if len(q)>0:
            current = q.popleft()
    return head
