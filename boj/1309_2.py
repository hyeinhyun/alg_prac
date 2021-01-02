import sys
num=int(input())
g=[0]*(num*2+1)
total=[0]*(num+1)

for i in range(num,0,-1):
    if i==num:
        g[i*2-1]=1
        g[i*2]=1
        total[num]=2
    elif i==num-1:
        g[i*2-1]=2
        g[i*2]=2
        total[num-1]=6    
        
    else:
        g[i*2-1]=total[(i*2+4)//2]+g[i*2+2]+1
        g[i*2]=total[(i*2+4)//2]+g[i*2+2]+1
        total[i]=g[i*2]*2+total[i+1]




print((sum(g)+1)%9901)