#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# import Tree
from Puzzle import Puzzle
from pandas import *

size = 4

p = Puzzle(size)
print(DataFrame(p.getBoard()).to_string(index=False, header=False))
p.shuffle(100)
print(" ")
print(DataFrame(p.getBoard()).to_string(index=False, header=False))

# print(p.getOriginalBoard())
