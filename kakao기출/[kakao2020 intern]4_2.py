#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  2 18:06:41 2021

@author: hihyun
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  2 11:15:59 2021

@author: hihyun
"""
from collections import defaultdict
def solution(board):
    q=[[0,0,0]]
    N=len(board)
    v=[[-1 for i in range(N)] for i in range(N)]
    #v=defaultdict(list)
    p=[[[10000000]*4 for i in range(N)] for i in range(N)]
    #v[str((0,0))]=[0,0]
    v[0][0]=0
    p[0][0]=[0,0,0,0]
    x=[1,-1,0,0]
    y=[0,0,-1,1]
    direction=[0,1,2,3]#d,u,l,r
    while q:
        cur=q.pop(0)
        for i in range(4):
            if cur[0]==0 and cur[1]==0:
                price=100
            elif cur[2]==0:
                if x[i]==1:
                    price=100
                elif x[i]==-1:
                    price=10000000
                else:
                    price=600
            elif cur[2]==1:
                if x[i]==-1:
                    price=100
                elif x[i]==1:
                    price=10000000
                else:
                    price=600
            elif cur[2]==2:
                if y[i]==-1:
                    price=100
                elif y[i]==1:
                    price=10000000
                else:
                    price=600
            else:
                if y[i]==1:
                    price=100
                elif y[i]==-1:
                    price=10000000
                else:
                    price=600                              
            next_x=cur[0]+x[i]
            next_y=cur[1]+y[i]
            
            if next_x>=0 and next_x<N and next_y>=0 and next_y<N:
                if board[next_x][next_y]==0:
                    new_c=p[cur[0]][cur[1]][cur[2]]+price
                    #p[next_x][next_y][i]=min(p[next_x][next_y][i],p[cur[0]][cur[1]][cur[2]]+price)
                    if v[next_x][next_y]==-1 or v[next_x][next_y]>=new_c:
                                p[next_x][next_y][i]=min(p[next_x][next_y][i],p[cur[0]][cur[1]][cur[2]]+price)
                                v[next_x][next_y]=p[next_x][next_y][i]
                                q.append([next_x,next_y,direction[i]])

        
    
    answer = min(p[N-1][N-1])
    print(answer)
    return answer
solution([[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0],[0,0,0,0,1,0,0,0],[0,0,0,1,0,0,0,1],[0,0,1,0,0,0,1,0],[0,1,0,0,0,1,0,0],[1,0,0,0,0,0,0,0]])
