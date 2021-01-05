#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 14:45:55 2020

@author: hihyun
"""
from collections import deque

def solution(board):
    q=deque([((0,0),(0,1))])
    visit=[((0,0),(0,1))]
    pre={str(((0,0),(0,1))):None}
    count={str(((0,0),(0,1))):0}
    N=len(board)
    answer=1000000

    while q:
        cur=q.popleft()
        if str((N-1,N-1)) in str(cur):
            if answer>count[str(cur)]:
                answer=count[str(cur)]
                
        #moving
        X=[-1,1,0,0]
        Y=[0,0,-1,1]
        cur_l_x=cur[0][0]
        cur_l_y=cur[0][1]
        cur_r_x=cur[1][0]
        cur_r_y=cur[1][1]
        for i in range(4):
            pos_x=X[i]
            pos_y=Y[i]
            cond1=cur_l_x+pos_x>=0 and cur_l_x+pos_x<N
            cond2=cur_r_x+pos_x>=0 and cur_r_x+pos_x<N
            cond3=cur_l_y+pos_y>=0 and cur_l_y+pos_y<N
            cond4=cur_r_y+pos_y>=0 and cur_r_y+pos_y<N
            if cond1 and cond2 and cond3 and cond4:
                next_val=((cur_l_x+pos_x,cur_l_y+pos_y),(cur_r_x+pos_x,cur_r_y+pos_y))
                if board[next_val[0][0]][next_val[0][1]]==0 and board[next_val[1][0]][next_val[1][1]]==0:
                    if next_val not in visit and next_val[::-1] not in visit:
                        q.append(next_val)
                        visit.append(next_val)
                        pre[str(next_val)]=cur
                        count[str(next_val)]=count[str(cur)]+1
        #rotation
        X=[-1,-1,1,1]
        Y=[-1,1,-1,1]
        if (cur_r_y-cur_l_y)**2>0: #가로
            if cur_r_y-cur_l_y>0:#R : 0,2 L : 1,3
                for i in range(4):
                    if i%2==0:
                        if cur_r_x+X[i]>=0 and cur_r_x+X[i]<N and cur_r_y+Y[i]>=0 and cur_r_y+Y[i]<N:
                            if board[cur_r_x+X[i]][cur_r_y+Y[i]]==0 and board[cur_r_x+X[i]][cur_r_y]==0:
                                next_val=((cur_r_x+X[i],cur_r_y),(cur_r_x,cur_r_y))
                                if next_val not in visit and next_val[::-1] not in visit:
                                    q.append(next_val)
                                    visit.append(next_val)
                                    pre[str(next_val)]=cur
                                    count[str(next_val)]=count[str(cur)]+1  
                    else:
                        if cur_l_x+X[i]>=0 and cur_l_x+X[i]<N and cur_l_y+Y[i]>=0 and cur_l_y+Y[i]<N:
                            if board[cur_l_x+X[i]][cur_l_y+Y[i]]==0 and board[cur_l_x+X[i]][cur_l_y]==0:
                                next_val=((cur_l_x,cur_l_y),(cur_l_x+X[i],cur_l_y))
                                if next_val not in visit and next_val[::-1] not in visit:
                                    q.append(next_val)
                                    visit.append(next_val)
                                    pre[str(next_val)]=cur
                                    count[str(next_val)]=count[str(cur)]+1    
            else:
                cur_l_x,cur_r_x=cur_r_x, cur_l_x
                cur_l_y,cur_r_y=cur_r_y, cur_l_y
                for i in range(4):
                    if i%2==0:
                        if cur_r_x+X[i]>=0 and cur_r_x+X[i]<N and cur_r_y+Y[i]>=0 and cur_r_y+Y[i]<N:
                            if board[cur_r_x+X[i]][cur_r_y+Y[i]]==0 and board[cur_r_x+X[i]][cur_r_y]==0:
                                next_val=((cur_r_x,cur_r_y),(cur_r_x+X[i],cur_r_y))
                                if next_val not in visit and next_val[::-1] not in visit:
                                    q.append(next_val)
                                    visit.append(next_val)
                                    pre[str(next_val)]=cur
                                    count[str(next_val)]=count[str(cur)]+1  
                    else:
                        if cur_l_x+X[i]>=0 and cur_l_x+X[i]<N and cur_l_y+Y[i]>=0 and cur_l_y+Y[i]<N:
                            if board[cur_l_x+X[i]][cur_l_y+Y[i]]==0 and board[cur_l_x+X[i]][cur_l_y]==0:
                                next_val=((cur_l_x+X[i],cur_l_y),(cur_l_x,cur_l_y))
                                if next_val not in visit and next_val[::-1] not in visit:
                                    q.append(next_val)
                                    visit.append(next_val)
                                    pre[str(next_val)]=cur
                                    count[str(next_val)]=count[str(cur)]+1                      
                
        else:#세로
            if cur_r_x-cur_l_x>0:#R : 0,2 L : 1,3
                for i in range(4):
                    if i//2==0:
                        if cur_r_x+X[i]>=0 and cur_r_x+X[i]<N and cur_r_y+Y[i]>=0 and cur_r_y+Y[i]<N:
                            if board[cur_r_x+X[i]][cur_r_y+Y[i]]==0 and board[cur_r_x][cur_r_y+Y[i]]==0:
                                next_val=((cur_r_x,cur_r_y+Y[i]),(cur_r_x,cur_r_y))
                                if next_val not in visit and next_val[::-1] not in visit:
                                    q.append(next_val)
                                    visit.append(next_val)
                                    pre[str(next_val)]=cur
                                    count[str(next_val)]=count[str(cur)]+1  
                    else:
                        if cur_l_x+X[i]>=0 and cur_l_x+X[i]<N and cur_l_y+Y[i]>=0 and cur_l_y+Y[i]<N:
                            if board[cur_l_x+X[i]][cur_l_y+Y[i]]==0 and board[cur_l_x][cur_l_y+Y[i]]==0:
                                next_val=((cur_l_x,cur_l_y),(cur_l_x,cur_l_y+Y[i]))
                                if next_val not in visit and next_val[::-1] not in visit:
                                    q.append(next_val)
                                    visit.append(next_val)
                                    pre[str(next_val)]=cur
                                    count[str(next_val)]=count[str(cur)]+1  
            else:
                cur_l_x,cur_r_x=cur_r_x, cur_l_x
                cur_l_y,cur_r_y=cur_r_y, cur_l_y     
                for i in range(4):
                    if i//2==0:
                        if cur_r_x+X[i]>=0 and cur_r_x+X[i]<N and cur_r_y+Y[i]>=0 and cur_r_y+Y[i]<N:
                            if board[cur_r_x+X[i]][cur_r_y+Y[i]]==0 and board[cur_r_x][cur_r_y+Y[i]]==0:
                                next_val=((cur_r_x,cur_r_y),(cur_r_x,cur_r_y+Y[i]))
                                if next_val not in visit and next_val[::-1] not in visit:
                                    q.append(next_val)
                                    visit.append(next_val)
                                    pre[str(next_val)]=cur
                                    count[str(next_val)]=count[str(cur)]+1  
                    else:
                        if cur_l_x+X[i]>=0 and cur_l_x+X[i]<N and cur_l_y+Y[i]>=0 and cur_l_y+Y[i]<N:
                            if board[cur_l_x+X[i]][cur_l_y+Y[i]]==0 and board[cur_l_x][cur_l_y+Y[i]]==0:
                                next_val=((cur_l_x,cur_l_y+Y[i]),(cur_l_x,cur_l_y))
                                if next_val not in visit and next_val[::-1] not in visit:
                                    q.append(next_val)
                                    visit.append(next_val)
                                    pre[str(next_val)]=cur
                                    count[str(next_val)]=count[str(cur)]+1

    return answer
board=[[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]
#board=[[0,0,1],[0,0,0],[1,0,0]]
print(solution(board))
