#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# import Tree
from Board import Board
from Node import Node
import sys


size = int(sys.argv[1])


goal = Board(size)
p = Board(size)
n = Node(state=p)
print(goal)
print()
print(p)
print()
n.getState().shuffle(1)
print(n.getState())
print()
finish = n.dfs(goal)
print(finish.getState())
print(finish.getCost())
print(finish.getDepth())
