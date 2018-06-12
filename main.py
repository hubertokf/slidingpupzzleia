#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# import Tree
from Puzzle import Puzzle
import time, resource, sys
# from memory_profiler import memory_usage

size = int(sys.argv[1])

p = Puzzle(size, moves=int(sys.argv[3]))
# print(p)
# print(" ")
# p.shuffle(int(sys.argv[3]))
# p.shuffle(10)
# print(p)

start = time.clock()
# print(" ")
# p.dfs()
# print(p)

if sys.argv[2] == "bfs":
    d = p.bfs()
elif sys.argv[2] == "dfs":
    d = p.dfs()
elif sys.argv[2] == "ids":
    d = p.ids()

time2 = time.clock() - start
mem_usage = format(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1000.0, '.2f')
print("Depth: {} Time: {} s Mem: {} MB".format(d, format(time2, '.7f'), mem_usage))
