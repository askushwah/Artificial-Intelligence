#search with akshay and ameya
#linear conflict refered stackover flow and github link and discussed with akshay
import sys
import time
import copy
import heapq
import math

#calculate heuristic g+h
def calculate_heuristic(board,level):
    mandist = 0
    for r in range(0,4):
        for c in range(0,4):
            if board[r][c]==0:continue
            mandist=mandist+(abs(r-(board[r][c]-1)/4)+abs(c-(board[r][c]-1)%4))
    mandist=int(math.ceil(float(mandist)/3))
    mandist=mandist+verticalconflict(board)
    mandist=mandist+horizontalconflict(board)
    return mandist+level

# horizontal linear conflicts
def horizontalconflict(board):
    linearconflict = 0
    for r in range(0, 4):
        max = -1
        for c in range(0, 4):
            if board[r][c] != 0 and (((board[r][c] - 1) / 4) == r):
                if board[r][c] > max:
                    max = board[r][c]
                else:
                    linearconflict += 2
    return linearconflict


# vertical linear conflicts
def verticalconflict(board):
    linearconflict = 0
    for c in range(0, 4):
        max = -1
        for r in range(0, 4):
            if board[r][c] != 0 and ((board[r][c]) % 4) == (c + 1) % 4:
                if board[r][c] > max:
                    max = board[r][c]
                else:
                    linearconflict += 2
    return linearconflict

#get all the succesors of a state in row left
def get_statesrowleft(state1,r,c,row):
    state=copy.deepcopy(state1)
    new_state= state[0:r] +[state[r][0:c] + [0, ] + state[r][c + 1:]] + state[r + 1:]
    temp=new_state[r][c]
    while c>row:
        new_state[r][c]=new_state[r][c-1]
        c-=1
    new_state[r][row]=temp
    return new_state

#get all the succesors of a state in row right
def get_statesrowright(state1,r,c,row):
    state=copy.deepcopy(state1)
    new_state= state[0:r] +[state[r][0:c] + [0, ] + state[r][c + 1:]] + state[r + 1:]
    temp=new_state[r][c]
    while c<row:
        new_state[r][c]=new_state[r][c+1]
        c+=1
    new_state[r][row]=temp
    return new_state

#get all the succesors of a state in column up
def get_statescolumnup(board,r,c,col):
    board = copy.deepcopy(board)
    new_state= board[0:r] +[board[r][0:c] + [0, ] + board[r][c + 1:]] + board[r + 1:]
    temp = new_state[r][c]
    while r>col:
        new_state[r][c] = new_state[r-1][c]
        r -= 1
    new_state[col][c] = temp
    return new_state

#get all the succesors of a state in column down
def get_statescolumndown(board,r,c,col):
    board = copy.deepcopy(board)
    new_state= board[0:r] +[board[r][0:c] + [0, ] + board[r][c + 1:]] + board[r + 1:]
    temp=new_state[r][c]
    while r<col:
        new_state[r][c]=new_state[r+1][c]
        r+=1
    new_state[col][c]=temp
    return new_state

#path state
def pathstate(board,r,c,cost,path):
    succ=[]
    for row in range(0, 4):
        if row < c:
            state = get_statesrowleft(board, r, c, row)
            s = ["R" + str(abs(c - row)) + str(r + 1)]  # row
            succ.append([calculate_heuristic(state,cost),cost,path+s,state])
        elif row > c:
            state = get_statesrowright(board, r, c, row)
            s = ["L" + str(abs(row - c)) + str(r + 1)]
            succ.append([calculate_heuristic(state, cost), cost,path+s ,state])
        if row < r:
            state1 = get_statescolumnup(board, r, c, row)
            s = ["D" + str(abs(r - row)) + str(c + 1)]  # col
            succ.append([calculate_heuristic(state1, cost), cost,path+s,state1])
        elif row > r:
            state1 = get_statescolumndown(board, r, c, row)
            s = ["U" + str(abs(row - r)) + str(c + 1)]
            succ.append([calculate_heuristic(state1, cost), cost,path+s,state1])
    return succ

# get all the successors
def successors(board,cost,path):

    for r in range(0,4):
        for c in range(0,4):
            if board[r][c]==0:
                return pathstate(board,r,c,cost,path)

def in_fringecloseoropen(s,fringe):
    for state in fringe:
        if state[3] == s[3]:
            return True
    return False

def solve(board):
    fringe_open=[]
    fringe_closed=[]
    if board==goal:
        return board
    heapq.heappush(fringe_open,[0,0,[],board])
    while len(fringe_open)>0:
        state = heapq.heappop(fringe_open)
        if in_fringecloseoropen(state, fringe_closed):
            continue
        fringe_closed.append(state)
        if state[3]==goal:
            #print "closed",len(fringe_closed)
            #print "open",len(fringe_open)
            return state
        for s in successors(state[3], state[1] + 1,state[2]):
            heapq.heappush(fringe_open,s)

goal=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,0]]
initial_board = [map(int,line.split()) for line in open("board.txt")]
start = time.time()
#print "solvable"
succ = solve(initial_board)
#for r in range(0,4):
#     for c in range(0,4):
#         print (succ[3])[r][c],
#     print ''
for r in range(0,len(succ[2])):
    sys.stdout.write((succ[2])[r],)
#end = time.time()
#print(end - start)
#print succ[0]
#print succ[1]
#print succ[2]
#print succ[3]