#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from Puzzle import Puzzle
import time, resource, sys

x3 = {
    10: [[0, 2, 3], [1, 5, 6], [4, 7, 8]],
    20: [[1, 3, 0], [7, 2, 5], [8, 4, 6]],
    30: [[1, 3, 6], [5, 8, 7], [4, 2, 0]],
    40: [[2, 3, 5], [8, 7, 4], [0, 1, 6]],
    50: [[5, 2, 3], [6, 0, 1], [4, 7, 8]]}

x2 = {
    10: [[1, 2], [3, 0]],
    20: [[0, 1], [3, 2]],
    30: [[0, 3], [2, 1]],
    40: [[0, 1], [3, 2]],
    50: [[0, 3], [2, 1]]}

size = int(sys.argv[1])
moves = int(sys.argv[2])
search = sys.argv[3]
h = ""

if size == 2:
    b = x2[moves]
else:
    b = x3[moves]

p = Puzzle(size, board=b)

start = time.clock()

if search == "bfs":
    d = p.bfs()
elif search == "dfs":
    d = p.dfs()
elif search == "ids":
    d = p.ids()
elif search == "a*":
    h = sys.argv[4]
    if h == "misplaced":
        d = p.a_star(p.misplaced)
    else:
        d = p.a_star(p.manhattan)

time2 = time.clock() - start
mem_usage = format(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1000.0, '.2f')
# print("Depth: {} Time: {} s Mem: {} MB".format(d, format(time2, '.7f'), mem_usage))
# algoritmo, heuristica, tamanho, embaralhamento, profundidade, tempo, memoria
print("{}, {}, {}, {}, {}, {}, {}".format(search, h, size, moves, d, format(time2, '.7f'), mem_usage))
