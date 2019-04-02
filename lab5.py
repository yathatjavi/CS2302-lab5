 # -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 10:04:14 2019

@author: Javier Soto
Professor Olac fuentes
TAs:
    -Anindita Nath
    -Maliheh Zaragaran
IA
    -Eduardo Lara
Peer Leader
    -Erick Macik
    

"""
import hash_table_chain_strings as HTC
import bst
import Wordnode as WN
from datetime import datetime as dt
import numpy as np


def startUp():
    #will prompt user to select data type and call metheod ac
    try:
        print("Choose table implementation")
        answer = int(input("Type 1 for binary search tree or 2 for hashtable with chaining"))
        print("Choice: ", end ="")
        print(str(answer))
        if answer == 1:
            print()
            print("Building binary search tree")
            buildBTree()
        elif int(answer) == 2:
            print()
            print("Building Hash Table")
            buildHTable()
        else:
            print("invalid input")
            print()
            startUp()
    except ValueError:
        print("exception reached")
        print()
        #startUp()
    
    
def buildHTable():
    #will read from file and create a hash table of words and there embeddings
    numWords =0
    initSize =9587
    myTable = HTC.HashTableC(initSize)
    
    buildStart = dt.now()
    #heFile = open('H:\Javis USB\CS2302\lab5\glove.6B.50d.txt', encoding = 'utf-8')
    theFile = open('G:\Javis USB\CS2302\lab5\glove.6B.50d.txt', encoding = 'utf-8')
    #theFile = open('G:\Javis USB\CS2302\lab5\reduced', encoding = 'utf-8')
    
    #while reading each line, crate a word node and add that new node to the table
    for line in theFile:
        numWords += 1
        tempNode = WN.Word(line)
        HTC.InsertC(myTable,tempNode)
    buildEnd = dt.now() - buildStart
    theFile.close()
    
    print()
    print("Hash table stats:")
    print("initial table size: " + str(initSize))
    
    while HTC.loadFactor(myTable)>1:
        myTable = HTC.resize(myTable)
        
    print("new table size " + str(len(myTable.item)))
    print("new load factor ", round(HTC.loadFactor(myTable), 4))
    print("Percentage of empty list: ", round(HTC.percentEmpty(myTable), 4))
    print("Standard deviation of lengths of lists: ", round(HTC.TableStandardDeviation(myTable),2))
    print('Running time for Hashtable construction: ' , buildEnd)
    print()
    print('Reading word file to determin similarities')
    print()
    
    read_test_file_hash(myTable)
    

def buildBTree():
     #will read from file and create a binary tree of words and there embeddings
     numWords =0
     #foo item used to create the tree outside the loop
     #item will be deleted once the tree is created
     fooNode = WN.Word("fooItem 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17")
     myTree = bst.BST(fooNode)
     
     buildStart = dt.now()
     #1theFile = open('H:\Javis USB\CS2302\lab5\glove.6B.50d.txt', encoding = 'utf-8')
     theFile = open('G:\Javis USB\CS2302\lab5\glove.6B.50d.txt', encoding = 'utf-8')
     #theFile = open('reduced.txt', encoding = 'utf-8')
     for line in theFile:
         numWords += 1
         tempNode = WN.Word(line)
         bst.Insert(myTree,tempNode)
     bst.Delete(myTree,fooNode)
     buildEnd = dt.now() - buildStart
     theFile.close()
     
     myTreeHeight = bst.MaxHeight(myTree)
     
     
     print()
     print('Binary Search Tree stats:')
     print('Number of nodes: ' + str(numWords) )
     print('max height is: ' + str(myTreeHeight))
     print('Running time for binary search tree construction: ' + str(buildEnd))
     print()
     print('Reading word file to determine similarities')
     print()
     similarites_bst(myTree)
     
     
     
def similarites_bst(T):
    #will take a tree as input 
    #will read a file of paired words search the tree for the embeddings of these words
    #will print the cosine distance of the two words
    print("Word similarities found:")
    st = dt.now()
    theFile2 = open('test.words.txt')
    for line in theFile2:
        words = line.split()
        #will be of type bst
        word_one_node = bst.Find(T,words[0])
        word_two_node = bst.Find(T,words[1])
        #call to cosineDistance with two word nodes and rounding the retuned value to the 4th decimal
        print("Similarity ", words, '=',round(cosineDistance(word_one_node.item,word_two_node.item), 4))
        
    endt = dt.now()-st
    print()
    print("Running time for binary search tree query processing: ", endt)
    
def read_test_file_hash(H):
    filePath = 'G:\Javis USB\CS2302\lab5\test.words.txt'
    #theFile2 = open(filePath)
    htqueryStart = dt.now()
    theFile2 = open('test.words.txt')
    for line in theFile2:
        
        words = line.split()
        word_one_node = HTC.FindWordNode(H,words[0])
        word_two_node = HTC.FindWordNode(H,words[1])
        #if word_one_node == -1 or word_two_node == -1:
         #   print('item not in list')
          #  return
        dist = cosineDistance(word_one_node,word_two_node)
        print('Similarity ', words ,' = ', round(dist,4))
    endtime = dt.now() -htqueryStart 
    print()
    print('Running time for hash table query processing ', endtime)
    
def cosineDistance(w1,w2):
#will take 2 word nodes and return the cosine distance between those two nodes
    
    dotP = np.dot(w1.embedding,w2.embedding)
    magW1= abs(magnitude(w1))
    magW2= abs(magnitude(w2))
    return dotP/(magW1*magW2)
    

def magnitude(item):
    #will take a word node and return the magnitude of the assosiated embedding
    return np.linalg.norm(item.embedding)

   

startUp()
        
