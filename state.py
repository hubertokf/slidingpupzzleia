#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from copy import deepcopy


class State:
    
    def operator(state):
        states = []

        zero_i = None
        zero_j = None

        for i in range(len(state)):
            for j in range(len(state)):
                if state[i][j] == 0:
                    zero_i = i
                    zero_j = j
                    break

        def add_swap(i, j):
            new_state = deepcopy(state)
            new_state[i][j], new_state[zero_i][zero_j] = new_state[zero_i][zero_j], new_state[i][j]
            states.append(new_state)

        if zero_i != 0:
            add_swap(zero_i - 1, zero_j)

        if zero_j != 0:
            add_swap(zero_i, zero_j - 1)

        if zero_i != len(state) - 1:
            add_swap(zero_i + 1, zero_j)

        if zero_j != len(state) - 1:
            add_swap(zero_i, zero_j + 1)

        return states
