#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  5 00:34:19 2017

@author: tejas, apoorva
"""
#from Initiate_Board import Board
from copy import deepcopy

#return tuple for cell
#import dictionary

scores = {3:1, 4:1, 5:2, 6:3, 7:5, 8:11}
validList = []

def updateScore(word):
    if (len(word) > 2):
        validList.append(word)
        return scores.get(len(word), 11)
    return 0

def Find_nbr(cell, BoardSize):
    nbr = []
    xlist = [cell[0], cell[0]+1, cell[0]-1]
    ylist = [cell[1],cell[1]+1,cell[1]-1]
    for i in xlist:
        for j in ylist:
            if i==cell[0] and j==cell[1]:
                continue
            elif i>=0 and j>=0 and i<BoardSize and j<BoardSize:
                nbr.append((i,j))
    return nbr

def DFS(board,root,visited,cell,word):
    neighbor = Find_nbr(cell, board.BoardSize) #list of neighbour tuples
    #word.append(board[cell[0]][cell[1]])
    score = 0
    for n in neighbor:
        visited_n = deepcopy(visited)
        if visited_n[n[0]][n[1]] == False:
            visited_n[n[0]][n[1]] = True
            word_n = deepcopy(word)
            word_n += board.matrix[n[0]][n[1]]
            #print('word: ', word_n) 
            (present,partial)=root.search(word_n)
            if (present):
                #print('present ',word_n)
                score += updateScore(word_n)              
            if (partial):
                #print('partial ',word_n)
                score += DFS(board,root,visited_n,n,word_n)
    return score

            