#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Tree():
    def __init__(self, value=None, children=None):
        self.value = value
        self.children = []
        self.parent = None
        # add information if is truncated
        if value is not None and children is not None:
            for child in children:
                self.addChild(child)

    def __repr__(self):
        return self.value
    
    def getValue(self):
        return self.value

    def setValue(self, val):
        self.value = val

    def getChildren(self):
        return self.children

    def addChild(self, node):
        assert isinstance(node, Tree)
        self.children.append(node)

        return self.children
    
    def findVal(self, val):
        if val < self.value:
            if self.left is None:
                return str(val)+" Not Found"
            return self.left.findval(val)
        elif val > self.value:
            if self.right is None:
                return str(val)+" Not Found"
            return self.right.findval(val)
        else:
            print(str(self.value) + ' is found')
