#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import Node


class Tree():
    def __init__(self):
        self.root = None

    def setRoot(self, val):
        self.root = Node(val)

    def insert(self, val):
        if(self.root is None):
            self.setRoot(val)
        else:
            self.insertNode(self.root, val)

    def insertNode(self, currentNode, val):
        if(val <= currentNode.val):
            if(currentNode.left):
                self.insertNode(currentNode.left, val)
            else:
                currentNode.left = Node(val)
        elif(val > currentNode.val):
            if(currentNode.right):
                self.insertNode(currentNode.right, val)
            else:
                currentNode.right = Node(val)

    def add_node(self, val, node=None):

        if node is None:
            node = self.root
        if self.root is None:
            self.root = Node(val)
        else:
            if val <= node.val:
                if node.left is None:
                    node.left = Node(val)
                    node.left.parent = node
                    print("left")
                    return
                else:
                    # return self.add_node(val,node = self.root.left)
                    return self.add_node(val, node=node.left)
            else:
                if node.right is None:
                    node.right = Node(val)
                    node.right.parent = node
                    print("right")
                    return
                else:
                    # return self.add_node(val,node = self.root.right)
                    return self.add_node(val, node=node.right)
    
    def search(self, val, node=None):

        if node is None:
            node = self.root

        if self.root.val == val:
            print("val is at the root")
            return self.root
        else:
            if node.val == val:
                print("val exists")
                return node

            elif val < node.val and node.left is not None:
                print("left")
                return self.search(val, node=node.left)
            elif val > node.val and node.right is not None:
                print("right")
                return self.search(val, node=node.right)
            else:
                print("val does not exist")
                return None

    def delete_node(self, val, node=None):
        # search for the node to be deleted in tree
        if node is None:
            node = self.search(val)  # return the node to be deleted

        # root has no parent node	
        if self.root.val == node.val:  # if it is root
            parent_node = self.root
        else:
            parent_node = node.parent
            
        '''case 1: The node has no chidren'''
        if node.left is None and node.right is None:
            if val <= parent_node.val:
                parent_node.left = None
            else:
                parent_node.right = None
            return

        '''case 2: The node has children'''
        ''' if it has a single left node'''
        if node.left is not None and node.right is None:
            if node.left.val < parent_node.val: 
                parent_node.left = node.left
            else:
                parent_node.right = node.left

            return

        '''if it has a single right node'''
        if node.right is not None and node.left is None:
            if node.val <= parent_node.val:
                parent_node.left = node.right
            else:
                parent_node.right = node.right
            return

        '''if it has two children'''
        '''find the node with the minimum value from the right subtree.
           copy its value to thhe node which needs to be removed.
           right subtree now has a duplicate and so remove it.'''
        if node.left is not None and node.right is not None:
            min_value = self.find_minimum(node)
            node.val = min_value.val
            min_value.parent.left = None
            return

    def find_minimum(self, node=None):
        
        if node is None:
            node = self.root

        '''find mimimum value from the right subtree'''
        
        '''case when there is only a root node'''
        if node.right is not None:
            node = node.right
        else:
            return node

        if node.left is not None:
            return self.find_minimum(node=node.left)
        else:
            return node

    def tree_data(self, node=None):
        if node is None:
            node = self.root

        stack = []
        while stack or node:
            if node is not None:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                yield node.val
                node = node.right
