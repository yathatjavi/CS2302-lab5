# Implementation of hash tabbles with chaining using strings
import numpy as np

class HashTableC(object):
    # Builds a hash table of size 'size'
    # Item is a list of (initially empty) lists
    # Constructor
    def __init__(self,size):  
        self.item = []
        self.num_items =0
        for i in range(size):
            self.item.append([])
        
        
def InsertC(H,k):
    # Inserts k in appropriate bucket (list) 
    # Does nothing if k is already in the table
    #b = h(k,len(H.item))
    b = HashCode(H,k)
    H.item[b].append([k]) 
    H.num_items +=1
   
    
def loadFactor(H):
    #will take a hastable as input and return the load factor
    return H.num_items/len(H.item)


def resize(H):
    #will take a hastable and double the size of the hash table
    tempTable = HashTableC(len(H.item)*2)
    for i in range(len(H.item)):
        for j in range(len(H.item[i])):
            #print(type(i))
            InsertC(tempTable, H.item[i][j][0])
    return tempTable


def FindC(H,k):
    # Returns bucket (b) and index (i) 
    # If k is not in table, i == -1
    #b = h(k,len(H.item))
    b = HashCode(H,k)
    for i in range(len(H.item[b])):
        if H.item[b][i][0].text == k:
            return b, i, H.item[b][i][1]
    return b, -1, -1


def TableStandardDeviation(H):
    buckts =[]
    for i in range(len(H.item)):
        buckts.append(len(H.item[i]))
    return np.std(buckts)


def FindWordNode(H,k):
    b = HashCodeString(H,k)
    for i in range(len(H.item[b])):
        if H.item[b][i][0].text == k:
            #return b, i, H.item[b][i][0]
            return  H.item[b][i][0]
    return b, -1, -1


def percentEmpty(H):
    #will take a hash table and return the percentaage of empty buckets
    emptybuckets =0
    for i in range(len(H.item)):
        if len(H.item[i]) <1:
            emptybuckets += 1
    return 100 * emptybuckets/len(H.item)
   
    
def h(s,n):
    r = 0
    for c in s:
        r = (r*n + ord(c))% n
    return r


def HashCodeString(H,item):
    #takes a string and returns the hashcode
    return hash(item)%len(H.item)


def HashCode(H,item):
    #takes a word node and retunes the hashcode
    return hash(item.text)%len(H.item)
'''
H = HashTableC(11)
A = ['data','structures','computer','science','university','of','texas','at','el','paso']
for a in A:
    InsertC(H,a,len(a))
    print(H.item)

for a in A: # Prints bucket, position in bucket, and word length
    print(a,FindC(H,a))
'''
 
