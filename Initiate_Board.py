#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  4 23:06:47 2017

@author: tejas, apoorva
"""
# Die
import random

Classic4 = [
    ['A', 'A', 'C', 'I', 'O', 'T'], ['A', 'B', 'I', 'L', 'T', 'Y'], ['A', 'B', 'J', 'M', 'O', 'Qu'],
    ['A', 'C', 'D', 'E', 'M', 'P'], ['A', 'C', 'E', 'L', 'R', 'S'], ['A', 'D', 'E', 'N', 'V', 'Z'],
    ['A', 'H', 'M', 'O', 'R', 'S'], ['B', 'F', 'I', 'O', 'R', 'X'], ['D', 'E', 'N', 'O', 'S', 'W'],
    ['D', 'K', 'N', 'O', 'T', 'U'], ['E', 'E', 'F', 'H', 'I', 'Y'], ['E', 'G', 'I', 'N', 'T', 'V'],
    ['E', 'G', 'K', 'L', 'U', 'Y'], ['E', 'H', 'I', 'N', 'P', 'S'], ['E', 'L', 'P', 'S', 'T', 'U'],
    ['G', 'I', 'L', 'R', 'U', 'W']
    ]
New4 = [
    ['A', 'A', 'E', 'E', 'G', 'N'], ['A', 'B', 'B', 'J', 'O', 'O'], ['A', 'C', 'H', 'O', 'P', 'S'],
    ['A', 'F', 'F', 'K', 'P', 'S'], ['A', 'O', 'O', 'T', 'T', 'W'], ['C', 'I', 'M', 'O', 'T', 'U'],
    ['D', 'E', 'I', 'L', 'R', 'X'], ['D', 'E', 'L', 'R', 'V', 'Y'], ['D', 'I', 'S', 'T', 'T', 'Y'],
    ['E', 'E', 'G', 'H', 'N', 'W'], ['E', 'E', 'I', 'N', 'S', 'U'], ['E', 'H', 'R', 'T', 'V', 'W'],
    ['E', 'I', 'O', 'S', 'S', 'T'], ['E', 'L', 'R', 'T', 'T', 'Y'], ['H', 'I', 'M', 'N', 'U', 'Qu'],
    ['H', 'L', 'N', 'N', 'R', 'Z']
    ]

class Board:
    diceinfo = Classic4 #if (BoardSize==4 && Rules=='Classic') else New4

    def __init__(self,BoardSize=4,Rules='Classic'):
        self.BoardSize = BoardSize
        self.Rules = Rules
        #self.matrix = [[] for i in range(BoardSize)]  
        self.matrix = []
        
    def populate(self):
        random.shuffle(Board.diceinfo)
        k = 0
        for i in range(self.BoardSize):
            list1 = []
            for j in range(self.BoardSize):
                index2 = random.randint(0,5)
                #self.matrix[i][j] = Board.diceinfo[k][index2]
                list1.append(Board.diceinfo[k][index2])
                k+=1
            self.matrix.append(list1)
    
    def __str__(self):
        return ''.join(str(r) for v in self.matrix for r in v)
                

        
