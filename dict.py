#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul  2 20:20:48 2017

@author: tejas, apoorva
"""
#Boggle
import collections

answer = collections.namedtuple('answer',['present','partial'])

class Node:
    def __init__(self,end=False):
        #self.letter = letter
        self.end = end
        self.childList = [None]*26
    
class Dict:
    def __init__(self):
        self.root = Node()
    
    def insert(self,word):
        nextNode = self.root
        for y in word:
          index = ord(y) - ord('a')
          if (nextNode.childList[index] == None):
             nextNode.childList[index] = Node()
          nextNode = nextNode.childList[index]
        nextNode.end = True
        
    def search(self,word):
        nextNode = self.root
        for y in word:
            index = ord(y) - ord('a')
            if (nextNode.childList[index] == None):
                #return False
                return answer(present=False,partial=False)
            nextNode = nextNode.childList[index]
        if (nextNode.end == True):
            #return True
            return answer(present=True,partial=True)
        else:
            #return False
            return answer(present=False, partial=True)
        
           


