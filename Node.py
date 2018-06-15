#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from copy import deepcopy
import random
from queue import Queue
from collections import deque


class Node:
    def __init__(self, state=None, parent=None, cost=0, depth=0, children=[], visited=False):
        self.state = state
        self.parent = parent
        self.children = children
        self.cost = cost
        self.depth = depth
        self.visited = visited

    def is_goal(self, goal_state):
        for i in range(len(goal_state)):
            for j in range(len(goal_state)):
                if goal_state[i][j] != goal_state[i][j]:
                    return False
        return True

    def getCost(self):
        return self.cost

    def getDepth(self):
        return self.depth

    def expand(self):
        new_states = self.state.generateMoves()
        # self.children = []
        for state in new_states:
            self.children.append(
                Node(state, self, self.cost + 1, self.depth + 1))

    def expandOneRandom(self):
        state = self.state.generateRandomMove()
        self.children.append(Node(state, self, self.cost + 1, self.depth + 1))

    def parents(self):
        current_node = self
        while current_node.parent:
            yield current_node.parent
            current_node = current_node.parent

    def g(self):
        costs = self.cost
        for parent in self.parents():
            costs += parent.cost

        return costs

    def getChildren(self):
        return self.children

    def getParent(self):
        return self.parent

    def addChildren(self, n):
        self.children.append(n)

        return self.children

    def getState(self):
        return self.state

    def visit(self):
        self.visited = True

        return self

    def dfs(self, goal):
        stack = []

        stack.append(self)
        current_node = stack.pop()

        while not current_node.state.isEqual(goal):
            current_node.expandOneRandom()

            for i in current_node.getChildren():
                stack.append(i)
            
            current_node = stack.pop()
            print(current_node.getState())

        return current_node

    def bfs(self, goal):
        queue = deque()

        current_node = self

        while not current_node.state.isEqual(goal):
            current_node.expand()
            for i in current_node.getChildren():
                queue.append(i)

            current_node = queue.popleft()

            # if current_node.parent is not None:
            #     del current_node.parent
            print(current_node.state)
            print()

        return current_node

    def dls(self, node, depth):
        status_compare = self.compare(node)

        if depth == 0 and status_compare:
            return True
        if depth > 0:

            blank_row, blank_cell = self.find_blank(node)
            directions = self.checkMovePossibilities(
                blank_row, blank_cell, node)

            for direction in directions:
                child = self.movePiece(
                    (blank_row, blank_cell), direction, deepcopy(node))

                found = self.dls(deepcopy(child), depth-1)

                if found is not None:
                    return found
        return None

    def ids(self):
        found = None
        for depth in count(0):
            found = self.dls(self.board, depth)
            if found:
                return depth

    # def manhattan(self, board=None):
    #     count = 0
    #     if board is not None:
    #         for i in range((self.size**2)-1):
    #             index = self.find(i + 1, board)

    #             row_diff = abs((i / self.size) - (index / self.size))
    #             col_diff = abs((i % self.size) - (index % self.size))

    #             count += (row_diff + col_diff)

    #         index = self.find_blank(board)
    #         row_diff = abs((((self.size**2)-1) / self.size) - (index / self.size))
    #         col_diff = abs((((self.size**2)-1) % self.size) - (index % self.size))
    #         count += (row_diff + col_diff)
    #     else:
    #         for i in range((self.size**2)-1):
    #             index = self.find(i + 1)

    #             row_diff = abs((i / self.size) - (index / self.size))
    #             col_diff = abs((i % self.size) - (index % self.size))

    #             count += (row_diff + col_diff)

    #         index = self.find_blank()
    #         row_diff = abs((((self.size**2)-1) / self.size) - (index / self.size))
    #         col_diff = abs((((self.size**2)-1) % self.size) - (index % self.size))
    #         count += (row_diff + col_diff)

    #     return count

    def manhattan_distance(self, board=None):
        count = 0
        if board is not None:
            for row in range(len(board)):
                for cell in range(len(board[row])):
                    if (self.solution[row][cell] == 0):
                        continue
                    for rows in range(len(self.solution)):
                        for cells in range(len(self.solution[rows])):
                            if (self.solution[rows][cells] == board[row][cell]):
                                count += (abs(cells - cell) + abs(rows - row))
                                break

        else:
            for row in range(len(self.board)):
                for cell in range(len(self.board[row])):
                    if (self.solution[row][cell] == 0):
                        continue
                    for rows in range(len(self.solution)):
                        for cells in range(len(self.solution[rows])):
                            if (self.solution[rows][cells] == self.board[row][cell]):
                                count += (abs(cells - cell) + abs(rows - row))
                                break

        return count

    def calculate_misplaced(self, board=None):
        count = 0
        if board is not None:
            for row in range(len(board)):
                for cell in range(len(board[row])):
                    if self.solution[row][cell] != board[row][cell]:
                        count += 1
        else:
            for row in range(len(self.board)):
                for cell in range(len(self.board[row])):
                    if self.solution[row][cell] != self.board[row][cell]:
                        count += 1

        return count
