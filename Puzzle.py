#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random


class Puzzle():
    def __init__(self, size, board=None):
        if (board is None):
            # board = np.arange(size*size).reshape(size, size)
            # board[size-1][size-1] = -1
            self.size = size
            self.moves = []
            self.board = [[cell + (row * size) for cell in range(1, size + 1)] for row in range(size)]
            self.board[size - 1][size - 1] = 0
            self.original_board = self.board
                    
        else:
            self.board = board

    def getBoard(self):
        return self.board

    def setBoard(self, board):
        self.board = board
        
    def getOriginalBoard(self):
        return self.original_board

    # Finds the 0 on the board. Returns a tuple: (row, cell)
    def find_blank(self):
        for row in range(len(self.board)):
            for cell in range(len(self.board[row])):
                if self.board[row][cell] == 0:
                    return (row, cell)
        raise Exception("Ops, Could not find the blank cell")

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

    def shuffle(self, moves=100):
        blank_row, blank_cell = self.find_blank()

        for i in range(moves):
            possibleDirections = self.checkMovePossibilities(blank_row, blank_cell)

            direction = random.choice(possibleDirections)
            self.moveBlank(direction)

            if direction == "u":
                blank_row -= 1
            elif direction == "d":
                blank_row += 1
            elif direction == "l":
                blank_cell -= 1
            elif direction == "r":
                blank_cell += 1

    def move(self):
        pass

    def moveBlank(self, direction):
        blank_row, blank_cell = self.find_blank()

        if direction == "u":
            self.board[blank_row][blank_cell] = self.board[blank_row - 1][blank_cell]
            self.board[blank_row - 1][blank_cell] = 0
            self.moves.append("u")

        elif direction == "d":
            self.board[blank_row][blank_cell] = self.board[blank_row + 1][blank_cell]
            self.board[blank_row + 1][blank_cell] = 0
            self.moves.append("d")

        elif direction == "r":
            self.board[blank_row][blank_cell] = self.board[blank_row][blank_cell + 1]
            self.board[blank_row][blank_cell + 1] = 0
            self.moves.append("r")

        elif direction == "l":
            self.board[blank_row][blank_cell] = self.board[blank_row][blank_cell - 1]
            self.board[blank_row][blank_cell - 1] = 0
            self.moves.append("l")
