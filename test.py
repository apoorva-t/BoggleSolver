#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul  2 23:45:58 2017

@author: tejas, apoorva
"""

#import dict
from dictionary import Dict
from Initiate_Board import Board
import solver
import time
import Initiate_Board
import sys
import display

#def __main__():
root = Dict()
with open('twl06.txt') as inputfile:
    next(inputfile)
    next(inputfile)
    for line in inputfile:
        w = line.strip()
        w = w.upper()
        root.insert(w)
        
start_time = time.time()
BoggleBoard = Board()
BoggleBoard.populate()

print(BoggleBoard.matrix)



visited = [[False for _ in range(BoggleBoard.BoardSize)] for _ in range(BoggleBoard.BoardSize)]
totalScore = 0
for i in range(BoggleBoard.BoardSize):
    for j in range(BoggleBoard.BoardSize):
        visited[i][j] = True
        word = ''.join(str(BoggleBoard.matrix[i][j]))
        totalScore += solver.DFS(BoggleBoard, root, visited, (i,j), word)
        visited[i][j] = False
print ("---- %s seconds before ----" % (time.time() - start_time))
soln = list(set(solver.validList))
print ("---- %s seconds after ----" % (time.time() - start_time))
print ('TotalScore = ', totalScore)
print ('Number of words = ',len(soln))
display.run_disp(BoggleBoard, soln)
