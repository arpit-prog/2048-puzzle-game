#!/usr/bin/env python
# coding: utf-8

# In[29]:


import random
def startgame():
    mat=[]
    for i in range(4):
        mat.append([0]*4)
    return mat


def add_2(mat):
    c=random.randint(0,3)
    d=random.randint(0,3)
    while mat[c][d]!=0:
        c=random.randint(0,3)
        d=random.randint(0,3)
    mat[c][d]=2
    return mat


def compress(mat):
    temp=[]
    for i in range(4):
        temp.append([0]*4)
    for i in range(4):
        k=0
        for j in range(4):
            if mat[i][j]!=0:
                temp[i][k]=mat[i][j]
                k+=1
    return temp



def merge(temp):
    for i in range(4):
        for j in range(3):
            if temp[i][j]==temp[i][j+1] and temp[i][j]!=0:
                temp[i][j]=temp[i][j+1]*2
                temp[i][j+1]=0
    return temp


def reverse(mat):
    temp=[]
    for i in range(4):
        temp.append([0]*4)
    for i in range(4):
        for j in range(4):
            temp[i][j]=mat[i][-j-1]
    return temp

def transpose(mat):
    temp=[]
    for i in range(4):
        temp.append([0]*4)
    for i in range(4):
        for j in range(4):
            temp[i][j]=mat[j][i]
    return temp
def move_left(mat):
    comp=compress(mat)
    merg=merge(comp)
    comp=compress(merg)
    return comp

def move_right(mat):
    right=reverse(mat)
    right_shift=compress(right)
    right_comp=merge(right_shift)
    mat=compress(right_comp)
    mat=reverse(mat)
    return mat


def move_up(mat):
    trans=transpose(mat)
    left_shift=compress(trans)
    left_comp=merge(left_shift)
    left_shift=compress(left_comp)
    mat=transpose(left_shift)
    return mat


def move_down(mat):
    trans=transpose(mat)
    rev=reverse(trans)
    movL=compress(rev)
    com=merge(movL)
    movL=compress(com)
    rev=reverse(movL)
    trans=transpose(rev)
    mat=trans
    return mat

def curr_state(mat):
    for i in range(4):
        for j in range(4):
            if mat[i][j]==2048:
                return "YOU WON !!!"
    for i in range(4):
        for j in range(4):
            if mat[i][j]==0:
                return 'MATCH IS GOING ON'
    for i in range(4):
        for j in range(3):
            if mat[i][j]==mat[i][j+1]:
                return "MATCH IS GOING ON"
    for i in range(4):
        for j in range(3):
            if mat[j][i]==mat[j+1][i]:
                return "MATCH IS GOING ON"
    return "YOU LOST !!!"
    
    
    
    
    
            
            
            
            
    
        
    
    
        


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




