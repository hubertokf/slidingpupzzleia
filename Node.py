#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Node():
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None

    def get(self):
        return self.val

    def set(self, val):
        self.val = val

    def getChildren(self):
        children = []
        if(self.left is not None):
            children.append(self.left)
        if(self.right is not None):
            children.append(self.right)
