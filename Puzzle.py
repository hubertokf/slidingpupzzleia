#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random
from pandas import *
import copy, time
from itertools import count


class Puzzle():
    def __init__(self, size, moves=None, board=None):
        if (board is None):
            self.size = size
            self.moves = []
            self.board = [[cell + (row * size) for cell in range(1, size + 1)] for row in range(size)]
            self.board[size - 1][size - 1] = 0                    
            self.solution = copy.deepcopy(self.board)
        else:
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

    def checkMove(self, origin, destination, board=None):
        if board is None:            
            if self.board[origin[0]][origin[1]] is 0 or self.board[destination[0]][destination[1]] is 0:
                if origin[0] is destination[0] or origin[1] is destination[1]: 
                    if (abs(origin[0] - destination[0]) is 1) or (abs(origin[1] - destination[1]) is 1):
                        return True
                    else:
                        raise Exception("Invalid movement. Must be Neighboors.")
                else:
                    raise Exception("Invalid movement. Must be in the axis.")
            else:
                raise Exception("Invalid movement. Must involve a blank position.")
        else:
            if board[origin[0]][origin[1]] is 0 or board[destination[0]][destination[1]] is 0:
                if origin[0] is destination[0] or origin[1] is destination[1]: 
                    if (abs(origin[0] - destination[0]) is 1) or (abs(origin[1] - destination[1]) is 1):
                        return True
                    else:
                        raise Exception("Invalid movement. Must be Neighboors.")
                else:
                    raise Exception("Invalid movement. Must be in the axis.")
            else:
                raise Exception("Invalid movement. Must involve a blank position.")

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
    
    def rdfs(G, discovered):
        depth = 0
        for all edges from discovered to w in G.adjacentEdges(v):
            if vertex w is not labeled as discovered:
                depth = depth + 1
                recursively call DFS(G, w)

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
