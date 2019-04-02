'''
 Code to implement a binary search tree 
 Programmed by Olac Fuentes
 Last modified February 27, 2019
modified By Javier Soto for use with lab %

*** I Javier Soto will be modifing this file to be used with my own "word" object***
please see Wordnode.py file
'''
class BST(object):
    # Constructor
    def __init__(self, item, left=None, right=None):  
        self.item = item
        self.left = left 
        self.right = right      
        
def Insert(T,newItem):
    if T == None:
        T =  BST(newItem)
    elif T.item.text > newItem.text:
        T.left = Insert(T.left,newItem)
    else:
        T.right = Insert(T.right,newItem)
    return T

def Delete(T,del_item):
    if T is not None:
        if del_item.text < T.item.text:
            T.left = Delete(T.left,del_item)
        elif del_item.text > T.item.text:
            T.right = Delete(T.right,del_item)
        else:  # del_item == T.item
            if T.left is None and T.right is None: # T is a leaf, just remove it
                T = None
            elif T.left is None: # T has one child, replace it by existing child
                T = T.right
            elif T.right is None:
                T = T.left    
            else: # T has two chldren. Replace T by its successor, delete successor
                m = Smallest(T.right)
                T.item.text = m.item.text
                T.right = Delete(T.right,m.item)
    return T
         
def InOrder(T):
    # Prints items in BST in ascending order
    if T is not None:
        InOrder(T.left)
        print(T.item,end = ' ')
        InOrder(T.right)
  
def InOrderD(T,space):
    # Prints items and structure of BST
    if T is not None:
        InOrderD(T.right,space+'   ')
        print(space,T.item)
        InOrderD(T.left,space+'   ')
  
def SmallestL(T):
    # Returns smallest item in BST. Returns None if T is None
    if T is None:
        return None
    while T.left is not None:
        T = T.left
    return T   
 
def Smallest(T):
    # Returns smallest item in BST. Error if T is None
    if T.left is None:
        return T
    else:
        return Smallest(T.left)

def Largest(T):
    if T.right is None:
        return T
    else:
        return Largest(T.right)   

def Find(T,k):
    # Returns the address of k in BST, or None if k is not in the tree
    if T is None or T.item.text == k:
        return T
    if T.item.text<k:
        return Find(T.right,k)
    return Find(T.left,k)
    
def FindAndPrint(T,k):
    f = Find(T,k)
    if f is not None:
        print(f.item,'found')
    else:
        print(k,'not found')
        
def MaxHeight(T):
    temp = T
    if T is None:
        return 0
    if T is not None:
        LeftH=  1+MaxHeight(temp.left)
        RightH= 1+ MaxHeight(temp.right)
        if LeftH > RightH:
            return LeftH
        else:
            return RightH
    
         
    
'''   
# Code to test the functions above
T = None
A = [70, 50, 90, 130, 150, 40, 10, 30, 100, 180, 45, 60, 140, 42]
for a in A:
    T = Insert(T,a)
    
InOrder(T)
print()
InOrderD(T,'')
print()

print(SmallestL(T).item)
print(Smallest(T).item)

FindAndPrint(T,40)
FindAndPrint(T,110)

n=60
print('Delete',n,'Case 1, deleted node is a leaf')
T = Delete(T,n) #Case 1, deleted node is a leaf
InOrderD(T,'')
print('####################################')

n=90      
print('Delete',n,'Case 2, deleted node has one child')      
T = Delete(T,n) #Case 2, deleted node has one child
InOrderD(T,'')
print('####################################')

n=70      
print('Delete',n,'Case 3, deleted node has two children') 
T = Delete(T,n) #Case 3, deleted node has two children
InOrderD(T,'')

n=40      
print('Delete',n,'Case 3, deleted node has two children') 
T = Delete(T,n) #Case 3, deleted node has two children
InOrderD(T,'')
'''