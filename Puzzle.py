#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np


class Puzzle():
    def __init__(self, size, board=None):
        if (board is None):
            self.board = np.arange(size*size).reshape(size, size)
                    
        else:
            self.board = board

    def getBoard(self):
        return self.board
    
    def setBoard(self, board):
        self.board = board
