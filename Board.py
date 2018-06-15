#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random
from pandas import *
from copy import deepcopy
from itertools import count


class Board():
    def __init__(self, size=3, board=None, relaxing=None):
        self.relaxing = relaxing
        self.moves = []
        if (board is None):
            self.board = [[cell + (row * size) for cell in range(1, size + 1)] for row in range(size)]
            self.board[size - 1][size - 1] = 0
            self.solution = deepcopy(self.board)
            self.size = size
        else:
            self.board = board
            self.size = len(board)

    def __repr__(self):
        return DataFrame(self.board).to_string(index=False, header=False)

    def getBoard(self):
        return self.board

    def getSize(self):
        return self.size

    def setBoard(self, board):
        self.board = board

    def setOriginalBoard(self, board):
        self.original_board = board

    def getOriginalBoard(self):
        return self.original_board

    # Finds the 0 on the board. Returns a tuple: (row, cell)
    def find_blank(self):
        for row in range(len(self.board)):
            for cell in range(len(self.board[row])):
                if self.board[row][cell] == 0:
                    return (row, cell)
        raise Exception("Ops, Could not find the blank cell")

    def find(self, element):
        for row in range(len(self.board)):
            for cell in range(len(self.board[row])):
                if self.board[row][cell] == element:
                    return (row, cell)
        raise Exception("Ops, Could not find the element")

    def _clear(self, position1, position2=None):
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

    def checkMove(self, origin, destination):
        if self.relaxing != "free" and self.relaxing != "misplaced" and self.relaxing != "manhattan":
            self._clear(origin, destination)
        if self.relaxing != "free" and self.relaxing != "misplaced":
            self._adj(origin, destination)
        if self.relaxing != "free":
            self._axis(origin, destination)

        return True

    def checkMovePossibilities(self, blank_row, blank_cell):
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

    def _move(self, origin, destination):
        try:
            self.checkMove(origin, destination)

            self.board[origin[0]][origin[1]], self.board[destination[0]][destination[1]] = self.board[destination[0]][destination[1]], self.board[origin[0]][origin[1]]

            return self.board
        except Exception as e:
            raise e

    def _moveToNew(self, origin, destination):
        try:
            self.checkMove(origin, destination)
            new_state = deepcopy(self)

            new_state._move(origin, destination)

            return new_state
        except Exception as e:
            raise e

    def generateMoves(self):
        states = []
        blank_row, blank_cell = self.find_blank()

        if blank_row != 0:
            states.append(self._moveToNew((blank_row, blank_cell), (blank_row - 1, blank_cell)))
            self.moves.append("u")
        if blank_row != (self.size-1):
            states.append(self._moveToNew((blank_row, blank_cell), (blank_row + 1, blank_cell)))
            self.moves.append("d")

        if blank_cell != 0:
            states.append(self._moveToNew((blank_row, blank_cell), (blank_row, blank_cell - 1)))
            self.moves.append("l")
        if blank_cell != (self.size-1):
            states.append(self._moveToNew((blank_row, blank_cell), (blank_row, blank_cell + 1)))
            self.moves.append("r")

        return states

    def generateRandomMove(self):
        blank_row, blank_cell = self.find_blank()
        directions = self.checkMovePossibilities(blank_row, blank_cell)
        direction = random.choice(directions)

        if direction == "u":
            return self._moveToNew((blank_row, blank_cell), (blank_row - 1, blank_cell))
        elif direction == "d":
            return self._moveToNew((blank_row, blank_cell), (blank_row + 1, blank_cell))
        elif direction == "l":
            return self._moveToNew((blank_row, blank_cell), (blank_row, blank_cell - 1))
        elif direction == "r":
            return self._moveToNew((blank_row, blank_cell), (blank_row, blank_cell + 1))

    def shuffle(self, moves=50):
        blank_row, blank_cell = self.find_blank()
        new_state = deepcopy(self)

        for i in range(moves):
            possibleDirections = self.checkMovePossibilities(blank_row, blank_cell)

            direction = random.choice(possibleDirections)

            if direction == "u":
                new_state = self._move((blank_row, blank_cell), (blank_row - 1, blank_cell))
                self.moves.append("u")
                blank_row -= 1
            elif direction == "d":
                new_state = self._move((blank_row, blank_cell), (blank_row + 1, blank_cell))
                self.moves.append("d")
                blank_row += 1
            elif direction == "l":
                new_state = self._move((blank_row, blank_cell), (blank_row, blank_cell - 1))
                self.moves.append("l")
                blank_cell -= 1
            elif direction == "r":
                new_state = self._move((blank_row, blank_cell), (blank_row, blank_cell + 1))
                self.moves.append("r")
                blank_cell += 1
    
        return new_state

    def isEqual(self, puzzle):
        # return self.board == puzzle.getBoard()
        if self.size == puzzle.getSize():
            for i in range(self.size):
                for j in range(self.size):
                    if puzzle.getBoard()[i][j] != self.board[i][j]:
                        return False
            
            return True
        else:
            raise Exception("Puzzle sizes are different.")
