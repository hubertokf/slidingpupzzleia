#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random
from pandas import *
import copy, time, math
from itertools import count
from operator import itemgetter
import heapq


class Puzzle():
    def __init__(self, size, moves=None, board=None, relaxing=None):
        self.relaxing = relaxing
        self.size = size
        self.moves = []
        if (board is None):
            self.board = [[cell + (row * size) for cell in range(1, size + 1)] for row in range(size)]
            self.board[size - 1][size - 1] = 0
            self.solution = copy.deepcopy(self.board)
        else:
            self.solution = [[cell + (row * size) for cell in range(1, size + 1)] for row in range(size)]
            self.solution[size - 1][size - 1] = 0   
            self.board = board

        if moves is None:
            self.original_board = copy.deepcopy(self.board)
        else:
            self.shuffle(moves)
            self.original_board = copy.deepcopy(self.board)

    def __repr__(self):
        return DataFrame(self.board).to_string(index=False, header=False)

    def getBoard(self):
        return self.board

    def setBoard(self, board):
        self.board = board

    def setOriginalBoard(self, board):
        self.original_board = board

    def getOriginalBoard(self):
        return self.original_board

    # Finds the 0 on the board. Returns a tuple: (row, cell)
    def find_blank(self, board=None):
        if board is None:
            for row in range(len(self.board)):
                for cell in range(len(self.board[row])):
                    if self.board[row][cell] == 0:
                        return (row, cell)
        else:
            for row in range(len(board)):
                for cell in range(len(board[row])):
                    if board[row][cell] == 0:
                        return (row, cell)
        raise Exception("Ops, Could not find the blank cell")

    def find(self, element, board=None):
        if board is None:
            for row in range(len(self.board)):
                for cell in range(len(self.board[row])):
                    if self.board[row][cell] == element:
                        return (row, cell)
        else:
            for row in range(len(board)):
                for cell in range(len(board[row])):
                    if board[row][cell] == element:
                        return (row, cell)
        raise Exception("Ops, Could not find the element")

    def checkMovePossibilities(self, blank_row, blank_cell, board=None):
        possibleDirections = []

        if blank_row != 0:
            possibleDirections.append("u")
        if blank_row != (self.size-1):
            possibleDirections.append("d")

        if blank_cell != 0:
            possibleDirections.append("l")
        if blank_cell != (self.size-1):
            possibleDirections.append("r")

        return possibleDirections

    def _clear(self, position1, position2=None, board=None):
        if board is not None:
            if board[position1[0]][position1[1]] is 0 or board[position2[0]][position2[1]] is 0:
                return True
            else:
                raise Exception(
                    "Invalid movement. Must involve a blank position.")
        else:
            if self.board[position1[0]][position1[1]] is 0 or self.board[position2[0]][position2[1]] is 0:
                return True
            else:
                raise Exception(
                    "Invalid movement. Must involve a blank position.")

    def _adj(self, position1, position2):
        if (abs(position1[0] - position2[0]) is 1) or (abs(position1[1] - position2[1]) is 1):
            return True
        else:
            raise Exception("Invalid movement. Must be Neighboors.")

    def _axis(self, position1, position2):
        if position1[0] is position2[0] or position1[1] is position2[1]:
            return True
        else:
            raise Exception("Invalid movement. Must be in the axis.")

    def checkMove(self, origin, destination, board=None):
        if board is not None:
            if self.relaxing != "free" and self.relaxing != "misplaced" and self.relaxing != "manhattan":
                self._clear(origin, destination, board)
            if self.relaxing != "free" and self.relaxing != "misplaced":
                self._adj(origin, destination)
            if self.relaxing != "free":
                self._axis(origin, destination)
        else:
            if self.relaxing != "free" and self.relaxing != "misplaced" and self.relaxing != "manhattan":
                self._clear(origin, destination, self.board)
            if self.relaxing != "free" and self.relaxing != "misplaced":
                self._adj(origin, destination)
            if self.relaxing != "free":
                self._axis(origin, destination)

        return True

    def shuffle(self, moves=100):
        blank_row, blank_cell = self.find_blank()

        for i in range(moves):
            possibleDirections = self.checkMovePossibilities(blank_row, blank_cell)

            direction = random.choice(possibleDirections)
            self.movePiece((blank_row, blank_cell), direction)

            if direction == "u":
                blank_row -= 1
            elif direction == "d":
                blank_row += 1
            elif direction == "l":
                blank_cell -= 1
            elif direction == "r":
                blank_cell += 1

        return self.board

    def reset(self):
        self.board = copy.deepcopy(self.original_board)

        return self.board

    def _move(self, origin, destination, board=None):
        try:
            if board is None:
                self.checkMove(origin, destination)

                piece = self.board[origin[0]][origin[1]]
                self.board[origin[0]][origin[1]] = self.board[destination[0]][destination[1]]
                self.board[destination[0]][destination[1]] = piece
            else:
                self.checkMove(origin, destination, board)

                piece = board[origin[0]][origin[1]]
                board[origin[0]][origin[1]] = board[destination[0]][destination[1]]
                board[destination[0]][destination[1]] = piece
        except Exception as e:
            raise e

    def movePiece(self, piece, direction, board=None):
        try:
            if board is None:
                if direction == "u":
                    self._move(piece, (piece[0] - 1, piece[1]))
                    self.moves.append("u")

                elif direction == "d":
                    self._move(piece, (piece[0] + 1, piece[1]))
                    self.moves.append("d")

                elif direction == "r":
                    self._move(piece, (piece[0], piece[1] + 1))
                    self.moves.append("r")

                elif direction == "l":
                    self._move(piece, (piece[0], piece[1] - 1))
                    self.moves.append("l")

                return self.board
            else:
                if direction == "u":
                    self._move(piece, (piece[0] - 1, piece[1]), board)
                    self.moves.append("u")

                elif direction == "d":
                    self._move(piece, (piece[0] + 1, piece[1]), board)
                    self.moves.append("d")

                elif direction == "r":
                    self._move(piece, (piece[0], piece[1] + 1), board)
                    self.moves.append("r")

                elif direction == "l":
                    self._move(piece, (piece[0], piece[1] - 1), board)
                    self.moves.append("l")

                return board

        except Exception as e:
            raise e

    def compare(self, board=None):
        if board is None:
            return self.board == self.solution
        else:
            return board == self.solution

    def dfs(self):
        list_procs = []
        depth = 0

        list_procs.append(copy.deepcopy(self.board))

        status_compare = self.compare()

        while not status_compare:
            blank_row, blank_cell = self.find_blank()
            directions = self.checkMovePossibilities(blank_row, blank_cell)
            direction = random.choice(directions)

            self.movePiece((blank_row, blank_cell), direction)
            list_procs.append(copy.deepcopy(self.board))

            status_compare = self.compare()
            depth = depth + 1

        return depth

    def bfs(self):
        list_procs = []
        # list_BFS = []
        depth = 0

        # list_procs.append(copy.deepcopy(self.board))
        # matrix = list_procs.pop()

        status_compare = self.compare()

        # list_BFS.append(copy.deepcopy(self.board))
        board_ref = copy.deepcopy(self.board)

        while not status_compare:
            blank_row, blank_cell = self.find_blank(board_ref)
            directions = self.checkMovePossibilities(blank_row, blank_cell, board_ref)

            for direction in directions:
                a = self.movePiece((blank_row, blank_cell), direction, copy.deepcopy(board_ref))
                list_procs.append(copy.deepcopy(a))

            board_ref = list_procs.pop(0)
            status_compare = self.compare(board_ref)
            # list_BFS.append(copy.deepcopy(board_ref))

            depth = depth + 1

        # self.board = copy.deepcopy(board_ref)
        return depth

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
                    (blank_row, blank_cell), direction, copy.deepcopy(node))

                found = self.dls(copy.deepcopy(child), depth-1)

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


    # def manhattan_distance(self, board=None):
    #     count = 0
    #     if board is not None:
    #         for row in range(len(board)):
    #             for cell in range(len(board[row])):
    #                 if (self.solution[row][cell] == 0):
    #                     continue
    #                 for rows in range(len(self.solution)):
    #                     for cells in range(len(self.solution[rows])):
    #                         if (self.solution[rows][cells] == board[row][cell]):
    #                             count += (abs(cells - cell) + abs(rows - row))
    #                             break

    #     else:
    #         for row in range(len(self.board)):
    #             for cell in range(len(self.board[row])):
    #                 if (self.solution[row][cell] == 0):
    #                     continue
    #                 for rows in range(len(self.solution)):
    #                     for cells in range(len(self.solution[rows])):
    #                         if (self.solution[rows][cells] == self.board[row][cell]):
    #                             print(count)
    #                             count += (abs(cell - cells) + abs(row - rows))
    #                             break

    #     return count
    
    def manhattan(self, board=None):
        count = 0
        if board is not None:
            for row in range(len(board)):
                for cell in range(len(board[row])):
                    pos1, pos2 = self.find(board[row][cell], self.solution)
                    if board[row][cell] != 0:
                        if pos1 != row or pos2 != cell:
                            count += abs(row - pos1) + abs(cell - pos2)
        else:
            for row in range(len(self.board)):
                for cell in range(len(self.board[row])):
                    pos1, pos2 = self.find(self.board[row][cell], self.solution)
                    if self.board[row][cell] != 0:
                        if pos1 != row or pos2 != cell:
                            count += abs(row - pos1) + abs(cell - pos2)

        return count

    def misplaced(self, board=None):
        count = 0
        if board is not None:
            for row in range(len(board)):
                for cell in range(len(board[row])):
                    if board[row][cell] != 0 and self.solution[row][cell] != board[row][cell]:
                        count += 1
        else:
            for row in range(len(self.board)):
                for cell in range(len(self.board[row])):
                    if self.board[row][cell] != 0 and self.solution[row][cell] != self.board[row][cell]:
                        count += 1
    
        return count

    def a_star(self, heuristic, board=None):
        list_A_star = []
        fila_1 = []
        fila_2 = []
        indice_1 = 0
        indice_2 = 0
        depth = 0

        status_compare = self.compare(self.board)
        list_A_star.append(copy.deepcopy(self.board))

        value_heuristic = heuristic(self.board)
        
        heapq.heappush(fila_1, (value_heuristic, indice_1, copy.deepcopy(self.board)))
        indice_1 += 1

        board_ref = heapq.heappop(fila_1)[-1]

        while not status_compare:
            blank_row, blank_cell = self.find_blank(board_ref)
            
            directions = self.checkMovePossibilities(blank_row, blank_cell, board_ref)

            for direction in directions:
                a = self.movePiece((blank_row, blank_cell), direction, copy.deepcopy(board_ref))

                value_heuristic = heuristic(a)

                F = depth + value_heuristic

                heapq.heappush(fila_1, (F, indice_1, copy.deepcopy(a)))
                indice_1 += 1

                heapq.heappush(fila_2, (F, indice_2, depth+1))
                indice_2 += 1

            board_ref = heapq.heappop(fila_1)[-1]

            depth = heapq.heappop(fila_2)[-1]
            
            list_A_star.append(board_ref)
            status_compare = self.compare(board_ref)

        return depth
