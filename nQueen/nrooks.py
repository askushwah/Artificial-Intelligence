#!/usr/bin/env python
# nrooks.py : Solve the N-Rooks problem!
# D. Crandall, 2016
# Updated by Zehua Zhang, 2017
#
# The N-rooks problem is: Given an empty NxN chessboard, place N rooks on the board so that no rooks
# can take any other, i.e. such that no two rooks share the same row or column.

import os
import numpy as np
import time
import sys

#myTime = time.localtime ()
#second1 = myTime[ 4 ] * 60 + myTime[ 5 ] 

def count_on_row(board, row):
    return sum (board[ row ])

    # Count # of pieces in given column

def count_on_col(board, col):
    return sum ([ row[ col ] for row in board ])
    # Count total # of pieces on board

def count_pieces(board):
    return sum ([ sum (row) for row in board ])

    # Return a string with the board rendered in a human-friendly format

def printable_board(board):

    for i in range (N):
        for j in range (N):
            if board[ i ][ j ] == 1:
                board[ i ][ j ] = 'R'
            elif [i,j]  == a:
                board[ i ][ j ] = 'X'
            else:
                board[ i ][ j ] = '_'
    return '\n'.join (' '.join (elems) for elems in board)

    #return "\n".join ([ " ".join ([ "R" if col else "_" for col in row ]) for row in board ])

    # Add a piece to the board at the given position, and return a new board (doesn't change original)


def add_piece(board, row, col):
    return board[ 0:row ] + [ board[ row ][ 0:col ] + [ 1, ] + board[ row ][ col + 1: ] ] + board[ row + 1: ]

    # Get list of successors of given board state

Configure = set([])
def successors2(board):
    a = []
    b = [add_piece (board, r, c) for r in range (0, N) for c in range (0, N)]
    for g in b:
        if sum(map(sum, g)) < N+1:
            if str(g) not in Configure:
                a.append(g)

    for k in b:
        Configure.add(str(k))
    return a

def is_goal(board):
    return count_pieces (board) == N and \
           all ([ count_on_row (board, r) <= 1 for r in range (0, N) ]) and \
           all ([ count_on_col (board, c) <= 1 for c in range (0, N) ]) and \
           all ([board[(int(sys.argv[3]))-1][(int(sys.argv[4]))-1] != 1 for i in a])

def solve(initial_board):
    fringe = [ initial_board ]
    while len (fringe) > 0:
        for s in successors2 (fringe.pop (0)):
            if is_goal (s):
                return (s)
            fringe.append (s)
    return False

N = int(sys.argv[2])
a= [(int(sys.argv[3]))-1, (int(sys.argv[4]))-1]
initial_board = [ [ 0 ] * N for i in range (N) ]

solution = solve (initial_board)
print (printable_board (solution) if solution else "Sorry, no solution found. :(")
