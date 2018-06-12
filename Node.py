#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Node():
    def __init__(self, val):
        self.val = val
        self.children = []
        self.parent = None
        self.depth = None
        self.visited = False
    
    def __repr__(self):
        return self.val

    def visit(self):
        self.visited = True

        return self

    def getValue(self):
        return self.val

    def setValue(self, val):
        self.val = val

    def getDepth(self):
        return self.depth

    def setDepth(self, depth):
        self.depth = depth

    def getParent(self):
        return self.parent

    def setParent(self, n):
        self.parent = n

    def getChildren(self):
        return self.children

    def addChildren(self, n):
        self.children.append(n)

        return self.children
