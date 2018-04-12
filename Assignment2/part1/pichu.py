#!/usr/bin/env python

import time
import numpy as np
import sys

start=time.time()

def allMoves():
	#List that captures all the possible moves in the board
    allPossibleMoves = []
    for i in range (0, 64):
		#timer to run the program for specified number of times.
        if time.time()-start>globaltimer-1:
            break
		#Find all the parakeet available on the board
        if pichu_board[ int (i / 8) ][ i % 8 ] == 'P':
            if move_Parakeet(i):
                allPossibleMoves = allPossibleMoves + move_Parakeet(i)
		#Find all the robin available on the board
        elif pichu_board[ int (i / 8) ][ i % 8 ] == 'R':
            if move_Robin(i):
                allPossibleMoves = allPossibleMoves + move_Robin (i)
		#Find all the nighthawk available on the board
        elif pichu_board[ int (i / 8) ][ i % 8 ] == 'N':
            if move_Nighthawk(i):
                allPossibleMoves = allPossibleMoves + move_Nighthawk (i)
		#Find all the bluejay available on the board
        elif pichu_board[ int (i / 8) ][ i % 8 ] == 'B':
            if move_Bluejay(i):
                allPossibleMoves = allPossibleMoves + move_Bluejay (i)
		#Find all the kingfisher available on the board
        elif pichu_board[ int (i / 8) ][ i % 8 ] == 'K':
            if move_Kingfisher(i):
                allPossibleMoves = allPossibleMoves + move_Kingfisher (i)
		#Find all the quetzal available on the board
        elif pichu_board[ int (i / 8) ][ i % 8 ] == 'Q':
            if move_Quetzal(i):
                allPossibleMoves = allPossibleMoves + move_Quetzal (i)

    return allPossibleMoves

def move_Parakeet(location):
    possibleMove = []
    row = int (location / 8)
    column = location % 8
    try:
        for i in range (-1, 2, 2):
            if -1 < column + i < 7 and -1 < row < 8:
				#Parakeet checks for all the opponent and capture them
                if ((pichu_board[row+1][column+i]).islower()) and location <= 48:
                    tempValue = pichu_board[row+1][column+i]
                    pichu_board[row][column] = '.'
                    pichu_board[row+1][column+i] = 'P'
                    possibleMove.append(str(row) + str (column) + str (row + 1) + str (column + i)+ tempValue)
                    pichu_board[ row ][ column ] = 'P'
                    pichu_board[ row+1 ][ column+i ] = tempValue
    except Exception as e:
        pass
    try:
        for i in range (-1, 2, 2):
            if -1 < column + i < 7 and -1 < row < 8:
				#Checks for the last column and if parakeet reaches there, it converts to Q
                if ((pichu_board[row+1][column+i]).islower()) and location >= 48:
                    tempValue = pichu_board[row+1][column+i]
                    pichu_board[row][column] = '.'
                    pichu_board[row+1][column+i] = 'Q'
                    possibleMove.append (str (column) + str (column + i) + tempValue+ 'Q' + 'P')
                    pichu_board[ row ][ column ] = 'P'
                    pichu_board[ row +1 ][ column+i ] = tempValue
    except Exception as e:
        pass

    try:
        if -1 < row < 9 and -1 < column < 8:
			#Checks for all the blank positions available around the parakeet
            if ('.' == pichu_board[row+1][column]) and location <= 56:
                tempValue = pichu_board[row+1][column]
                pichu_board[row][column] = '.'
                pichu_board[row+1][column] = 'P'
                possibleMove.append(str (row)+ str (column) + str (row + 1) + str (column) + tempValue)

                pichu_board[ row ][ column ] = 'P'
                pichu_board[ row+1 ][ column ] = tempValue
    except Exception as e:
        pass

    try:
        if -1 < column+i  <= 7 and -1 < row < 8:
			#Code for moving parakeet one step forward
            if '.' == pichu_board[row+1][column] and location >= 48:
                tempValue = pichu_board[row+1][column]
                pichu_board[row][column] = '.'
                pichu_board[row+1][column] = 'Q'
                possibleMove.append (str(column)+ str (column)+tempValue+'Q'+'P')
                pichu_board[ row ][ column ] = 'P'
                pichu_board[ row +1 ][ column ] = tempValue
    except Exception as e:
        pass

    try:
		#Condition for moving parakeet 2 step forward
        if ('.' == pichu_board[row+1][column]) and ('.' == pichu_board[row+2][column])and location <= 16:
            tempValue = pichu_board[row+2][column]
            pichu_board[row][column] = '.'
            pichu_board[row+2][column] = 'P'
            possibleMove.append (str (row) + str (column) + str (row + 2)+ str (column)+ tempValue)
            pichu_board[ row ][ column ] = 'P'
            pichu_board[ row+ 2 ][ column ] = tempValue
    except Exception as e:
        pass
    return possibleMove

def move_Robin(location):
    possibleMove = []
    robinDirections = 1
    row = int (location / 8)
    column = location % 8
    for i in range (-1, 2, 2):
        try:
            if row >= 0:
				#The while condition keeps on going till the last of the board until it finds the other piece. And also it moves the robin in all column
                while '.' == pichu_board[ row ][ column + robinDirections * i ] and column + robinDirections * i >= 0:
                    tempValue = pichu_board[ row ][ column + robinDirections * i ]
                    pichu_board[ row ][ column ] = '.'
                    pichu_board[ row ][ column + robinDirections * i ] = 'R'
                    possibleMove.append (str (row)+str (column)+str (row)+str (column + robinDirections * i)+ tempValue+'r')
                    pichu_board[ row ][ column ] = 'R'
                    pichu_board[ row ][ column + robinDirections * i ] = tempValue
                    robinDirections = robinDirections + 1
				#This conditions tells about all the opponent players which falls in the range of robins
                if (pichu_board[ row ][ column + robinDirections * i ]).islower () and column + robinDirections * i>=0:
                    tempValue = pichu_board[ row ][ column + robinDirections * i ]
                    pichu_board[ row ][ column ] = '.'
                    pichu_board[ row ][ column + robinDirections * i ] = 'R'
                    possibleMove.append (str (row) + str (column) + str (row) + str (column + robinDirections * i) + tempValue+'r')
                    pichu_board[ row ][ column ] = 'R'
                    pichu_board[ row ][ column + robinDirections * i ] = tempValue
        except Exception:
            pass
        robinDirections = 1
        try:
            if row + robinDirections * i > 0 and column >= 0:
				#This section moves the robin in row direction
                while '.' == pichu_board[ row + robinDirections * i ][ column ] and row + robinDirections * i>=0:
                    tempValue = pichu_board[ row + robinDirections * i ][ column ]
                    pichu_board[ row ][ column ] = '.'
                    pichu_board[ row + robinDirections * i ][ column ] = 'R'
                    possibleMove.append(str (row) + str (column) + str (row + robinDirections * i)+ str (column)+ tempValue+'r')
                    pichu_board[ row ][ column ] = 'R'
                    pichu_board[ row + robinDirections * i ][ column ] = tempValue
                    robinDirections = robinDirections + 1
                if (pichu_board[ row + robinDirections * i ][ column ]).islower () and row + robinDirections * i>=0:
                    tempValue = pichu_board[ row + robinDirections * i ][ column ]
                    pichu_board[ row ][ column ] = '.'
                    pichu_board[ row + robinDirections * i ][ column ] = 'R'
                    possibleMove.append (str (row)+ str (column) + str (row + robinDirections * i)+ str (column)+ tempValue+'r')
                    pichu_board[ row ][ column ] = 'R'
                    pichu_board[ row + robinDirections * i ][ column ] = tempValue
        except Exception:
            pass
        robinDirections = 1
    return possibleMove

def move_Nighthawk(location):
    possibleMoves = []
    row = int (location / 8)
    column = location % 8
    for i in range (-1, 2, 2):
        for j in range (-1, 2, 2):
            try:
                if row + i >= 0 and column + j * 2 >= 0:
				#The loop is so formed as to make the nighthawk move in only diagonals. It either goes -1 or +1 ignoring 0.
                    if (pichu_board[ row + i ][ column + j * 2 ]).islower () or pichu_board[ row + i ][column + j * 2 ] == ".":
                        tempValue = pichu_board[ row + i ][ column + j * 2 ]
                        pichu_board[ row ][ column ] = "."
                        pichu_board[ row + i ][ column + j * 2 ] = "N"
                        possibleMoves.append (str (row) + str (column)+str (row + i)+str (column + j * 2)+ tempValue)
                        pichu_board[ row ][ column ] = "N"
                        pichu_board[ row + i ][ column + j * 2 ] = tempValue
            except Exception:
                pass
            try:
			#Condition to check that the board does not go in negative direction
                if row + i *2 >= 0 and column + j >=0:
					#Checks for the other direction in which nighthawk can move.
                    if (pichu_board[ row + i * 2 ][ column + j ]).islower () or pichu_board[ row + i * 2 ][column + j ] == ".":
                        tempValue = pichu_board[ row + i * 2 ][ column + j ]
                        pichu_board[ row ][ column ] = "."
                        pichu_board[ row + i * 2 ][ column + j ] = "N"
                        possibleMoves.append (str (row) + str (column) + str (row + i * 2)+ str (column + j)+ tempValue)
                        pichu_board[ row ][ column ] = "N"
                        pichu_board[ row + i * 2 ][ column + j ] = tempValue
            except Exception:
                pass

    return possibleMoves
	
#In bluejay also we calculate every possible direction in which it can move. The conditions are implemented in the loop below.
def move_Bluejay(location):
    possibleMoves = []
    quetzalDirections = 1
    row = int (location / 8)
    column = location % 8
    for i in range (-1, 2, 2):
        for j in range (-1, 2, 2):
            try:
				#While the board can go in negative direction and can cause unexpected behavior, a safe condition is applied throughout every case
                if row + quetzalDirections * i >= 0 and column + quetzalDirections * j >= 0:
                    while pichu_board[ row + quetzalDirections * i ][ column + quetzalDirections * j ] == '.' and column + quetzalDirections * j >= 0 and row + quetzalDirections * i>=0:
                        tempValue = pichu_board[ row + quetzalDirections * i ][ column + quetzalDirections * j ]
                        pichu_board[ row ][ column ] = '.'
                        pichu_board[ row + quetzalDirections * i ][ column + quetzalDirections * j ] = 'B'
                        possibleMoves.append (str (row) + str (column) + str (row + quetzalDirections * i)+ str (column + quetzalDirections * j)+ tempValue+'b')
                        pichu_board[ row ][ column ] = 'B'
                        pichu_board[ row + quetzalDirections * i ][ column + quetzalDirections * j ] = tempValue
                        quetzalDirections = quetzalDirections + 1

                    if (pichu_board[ row + quetzalDirections * i ][ column + quetzalDirections * j ]).islower () and column + quetzalDirections * j >= 0 and row + quetzalDirections * i>=0:
                        tempValue = pichu_board[ row + quetzalDirections * i ][ column + quetzalDirections * j ]
                        pichu_board[ row ][ column ] = '.'
                        pichu_board[ row + quetzalDirections * i ][ column + quetzalDirections * j ] = 'B'
                        possibleMoves.append(str (row) + str (column) + str (row + quetzalDirections * i) + str (column + quetzalDirections * j) + tempValue+'b')
                        pichu_board[ row ][ column ] = 'B'
                        pichu_board[ row + quetzalDirections * i ][ column + quetzalDirections * j ] = tempValue
            except Exception:
                pass
            quetzalDirections = 1
    return possibleMoves

#This is a simplest of all :). This just checks for all the possible moves around it. As it can move in every direction but only one step
def move_Kingfisher(location):
    list = []
    row = int (location / 8)
    column = location % 8
    for i in range (0, 9):
        row_check = row - 1 + int (i / 3)
        col_check = column - 1 + i % 3

        try:
            if row_check >= 0 and col_check >= 0 and i != 4 and (
                        (pichu_board[ row_check ][ col_check ]).islower () or
                            pichu_board[ row_check ][ col_check ] == '.'):
                old_piece = pichu_board[ row_check ][ col_check ]
                pichu_board[ row ][ column ] = '.'
                pichu_board[ row_check ][ col_check ] = 'K'
                list.append(str (row)+ str (column)+ str (row_check)+ str (col_check)+ old_piece+'a')
                pichu_board[ row ][ column ] = "K"
                pichu_board[ row_check ][ col_check ] = old_piece
        except Exception:
            pass
    return list

def move_Quetzal(location):
    possibleMoves = []
    quetzalDirections = 1
    row = int (location / 8)
    column = location % 8
    for i in range (-1, 2):
        for j in range (-1, 2):
                try:
				#Same goes with quetzal. There are conditions to be implemented for all possile moves with all the stopping conditions as well.
                    if row + quetzalDirections * i >= 0 and column + quetzalDirections * j > 0:
                        while pichu_board[ row + quetzalDirections * i ][ column + quetzalDirections * j ] == '.' and column + quetzalDirections * j >= 0 and row + quetzalDirections * i>=0:
                            tempValue = pichu_board[ row + quetzalDirections * i ][ column + quetzalDirections * j ]
                            pichu_board[ row ][ column ] = '.'
                            pichu_board[ row + quetzalDirections * i ][ column + quetzalDirections * j ] = 'Q'
                            possibleMoves.append(str (row)+ str (column)+str (row + quetzalDirections * i)+ str (column + quetzalDirections * j)+ tempValue+'q')
                            pichu_board[ row ][ column ] = 'Q'
                            pichu_board[ row + quetzalDirections * i ][ column + quetzalDirections * j ] = tempValue
                            quetzalDirections = quetzalDirections + 1

                        if (pichu_board[ row + quetzalDirections * i ][ column + quetzalDirections * j ]).islower () and column + quetzalDirections * j >= 0 and row + quetzalDirections * i>=0:
                            tempValue = pichu_board[ row + quetzalDirections * i ][ column + quetzalDirections * j ]
                            pichu_board[ row ][ column ] = '.'
                            pichu_board[ row + quetzalDirections * i ][ column + quetzalDirections * j ] = 'Q'
                            possibleMoves.append (str (row)+ str (column)+str (row + quetzalDirections * i)+ str (column + quetzalDirections * j)+ tempValue+'q')
                            pichu_board[ row ][ column ] = 'Q'
                            pichu_board[ row + quetzalDirections * i ][ column + quetzalDirections * j ] = tempValue
                except Exception:
                    pass
                quetzalDirections = 1
    return possibleMoves

#This moves the pience forward it it is blank.
#The format of the string is in "OriginalRow,OriginalColumn,FutureRow,FutureColumn,PieceToCapture"
def forward_move(move_piece):    #makeMove
    #print move
    if move_piece[4] is not 'P': #This checks for is it is not Parakeet. The basic of this function is that it swaps the position of the piece.
        pichu_board[int(move_piece[2])][int(move_piece[3])] = pichu_board[int(move_piece[0])][int(move_piece[1])]
        pichu_board[int(move_piece[0])][int(move_piece[1])] = '.'
    else:
        pichu_board[6][int(move_piece[0])] = '.'
        pichu_board[7][int(move_piece[1])] = move_piece[3]

#This is same as forward_move other then it moves the piece back.
def backward_move(move_piece):    #undoMove
    if move_piece[4] is not 'P':
        pichu_board[int(move_piece[0])][int(move_piece[1])] = pichu_board[int(move_piece[2])][int(move_piece[3])]
        pichu_board[int(move_piece[2])][int(move_piece[3])] = move_piece[4]
    else:
        pichu_board[6][int(move_piece[0])] = 'P'
        pichu_board[7][int(move_piece[1])] = move_piece[2]

def rateMaterial(): #function for rating various pieces on the board
    counter=0
    bluejayCounter=0
    for i in range(64):
        if pichu_board[int(i/8)][i%8]=='P': #Weightage for parakeet
            counter+=100
        elif pichu_board[int(i/8)][i%8]=='R': #Weightage for robin
            counter+=500
        elif pichu_board[int(i/8)][i%8]=='N': #Weightage for Nighthawk
            counter+=300
        elif pichu_board[int(i/8)][i%8]=='B': #Weightage for Blue Jay
            bluejayCounter+=1
        elif pichu_board[int(i/8)][i%8]=='Q': #Weightage for Quantezel
            counter+=900
        elif pichu_board[int(i/8)][i%8]=='K': #Weightage for Kingfisher
            counter+=1700
    if bluejayCounter>=2:  #Two bluejay can cover the entire board diagonally,so higher weightage
        counter+=300*bluejayCounter
    else:
        if bluejayCounter==1:  #One bluejay can cover only half the board,so less weightage
            counter+=250
    return counter

def rateMoveability(length,depth):  #Heuristic for number of possible moves
    counter=0
    counter+=length  #Adding the length of possible successors of the current state
    return counter

def move_rating(length,depth):  #Heuristic function
    counter=0
    counter+=rateMaterial()
    counter+=rateMoveability(length,depth)
    next_turn()
    counter-=rateMaterial()
    counter-=rateMoveability(length,depth)
    next_turn()
    return -(counter+depth*50)  #Giving weightage to the depth of the tree searched

def sortMoves(list_moves):  #Sort the list_moves to keep the best 7 moves at the beginning of the list
    score=[]
    for i in range(len(list_moves)):
        forward_move(list_moves[i])  #Make the move 
        score.append(-move_rating(-1,0))  #Calculate the score(rating) for the move
        backward_move(list_moves[i])  #Undo the move
    length=min(7,len(list_moves))
    A=list(sorted(zip(score,list_moves),reverse=True)[:length]) #Sort the list according to the score(rating)
    newListA=[]
    newListB=list_moves
    for i in range(length):
        newListA.append(A[i][1])
        newListB.remove(A[i][1])
    return newListA+newListB

def alphabeta(depth,beta,alpha,move,player):    
    list_moves=allMoves()  #All the possible successors of the current state
    if depth==0 or len(list_moves)==0:  #Stopping condition for recursion
        move.append(move_rating(len(list_moves),depth)*(player*2-1))
        return move
    player=1-player    #To change from Max to min node & Vice versa
    list_moves=sortMoves(list_moves)  #Keep the best 7 moves at the beginning of the list
    for i in range(len(list_moves)):
        forward_move(list_moves[i])  #Move the piece to the specified location
        next_turn()   #Flip the Board configuration so that the functions written remains reusable for both the players
        recursion=alphabeta(depth-1,beta,alpha,list_moves[i].split(),player)  #Recursively call the alpha beta function with lower depth & optimal successor
        value=recursion[1]   #Store the utilty value of the successor state
        next_turn()   #Flip the Board configuration for the other part of the tree
        backward_move(list_moves[i])  #To regain the original state
        if player==0:
            if value<=beta:
                beta=value   #Choose the maximum of all the MIN nodes
                if depth==final_depth:  #Traverse till final_Depth of the tree
                    move=recursion[0]
        else:
            if value>alpha:
                alpha=value  #Choose the minimum of all the MAX nodes
                if depth==final_depth:   #Traverse till final_Depth of the tree
                    move=recursion[0]
        if alpha>=beta:
            if player==0:   #Max node
                if type(move)==str:
                    move=move.split()
                move.append(beta)
                return move
            else:           #Min node
                if type(move)==str:
                    move=move.split()
                move.append(alpha)
                return move
    if player==0:
        if type(move)==str:
            move=move.split()
        move.append(beta)
        return move
    else:
        if type(move)==str:
            move=move.split()
        move.append(alpha)
        return move

#Prepare the board for the other player
def next_turn():
    for i in range(32):
        r=int(i/8)
        c=i%8
        if pichu_board[r][c].isupper():  #if the piece is in uppercase,convert it into lowercase 
            temp=pichu_board[r][c].lower()
        else:    #if the piece is in lowercase,convert it into uppercase
            temp=pichu_board[r][c].upper()
        if pichu_board[7-r][7-c].isupper():
            pichu_board[r][c]=pichu_board[7-r][7-c].lower()
        else:
            pichu_board[r][c]=pichu_board[7-r][7-c].upper()
        pichu_board[7-r][7-c]=temp

final_depth = 10  #Depth of the tree to be searched
globaltimer = int(sys.argv[ 3 ])   #timer value
new_board = str(sys.argv[ 2 ])   #initial board position
player = sys.argv[1]    #which player's turn to play?
data = np.array( list(new_board) )
format_board = ( 8, 8 )

pichu_board = data.reshape( format_board )

if player=='w':   #white move
    forward_move(alphabeta(final_depth, 1500000,-1500000,[],0)[0])
else:             #black move
    next_turn()
    forward_move(alphabeta(final_depth, 1500000,-1500000,[],1)[0])
    next_turn()
print(''.join(''.join(p) for p in pichu_board))
