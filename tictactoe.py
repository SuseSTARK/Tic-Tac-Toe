# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 15:35:45 2020

@author: susen
"""

import numpy as np
import random as rd

def gameboard():
     print(board[0],"   ",board[1],"   ",board[2])
     print("\n")
     print(board[3],"   ",board[4],"   ",board[5])
     print("\n")
     print(board[6],"   ",board[7],"   ",board[8])
     
def Win(char,c):
  global result
  if board[0]==board[1]==board[2]:
    if board[0]==char :
      print ("You win!!")
    elif board[0]==c:
      print ("Computer wins!!")
    result = True
  elif board[3]==board[4]==board[5]:
    if char == board[3]:
      print ("You win!!")
    elif board[3]==c:
      print ("Computer wins!!")
    result = True
  elif board[6]==board[7]==board[8]:
    if char == board[6]:
      print ("You win!!")
    elif board[6]==c:
      print ("Computer wins!!")
    result = True
  elif board[0]==board[3]==board[6]:
    if char == board[0]:
      print ("You win!!")
    elif board[0]==c:
      print ("Computer wins!!")
    result = True
  elif board[1]==board[4]==board[7]:
    if char == board[1]:
      print ("You win!!")
    elif board[1]==c:
      print ("Computer wins!!")
    result = True
  elif board[2]==board[5]==board[8]:
    if char == board[2]:
      print ("You win!!")
    elif board[2]==c:
      print ("Computer wins!!")
    result = True
  elif board[0]==board[4]==board[8]:
    if char == board[0]:
      print ("You win!!")
    elif board[0]==c:
      print ("Computer wins!!")
    result = True
  elif board[2]==board[4]==board[6]:
    if char == board[2]:
      print ("You win!!")
    elif board[2]==c:
      print ("Computer wins!!")
    result = True
    
board=np.zeros([9,1],dtype=int)
ctr=1
ctr=1
pos=np.array([[1,2,3],[4,5,6],[7,8,9]])
print("TIC TAC TOE\n")
print("X-1")
print("O-2")
ch=int(input("Enter your choice.\n"))
while ch!=1 and ch!=2:
    ch=int(input("Enter your choice.\n"))
    print(ch)
print("\n\n")

gameboard()
print("\n")

print("Corresponding positions for the matrix.\n")
for i in range(3):
    print(pos[i][0],"  ",pos[i][1],"  ",pos[i][2])
    print("\n")

if ch==1:
    c_ch=2
else:
    c_ch=1
user_pos=[]
c_pos=[]
for i in range(5):
    loc=int(input("Enter the desired position.\n"))
    flag=1
    while flag==1:
        if loc>=1 and loc<=9:
            flag=0
        if board[loc-1][0]==0:
            flag=0
        if flag==1:
            loc=int(input("Enter a valid position.\n"))
    
    board[loc-1][0]=ch
    gameboard()
    if i>=2:
        Win(ch,c_ch)
        print(result)
        if result==True:
            print("Gameover\n")
            break
    print("\n Computer is playing!\n")
    rd.seed()
    flag_c=1
    while flag_c==1:
        c_loc=rd.randrange(1,10)
        if board[c_loc-1][0]==0:
            flag_c=0
    board[c_loc-1][0]=c_ch
    gameboard()
    

    