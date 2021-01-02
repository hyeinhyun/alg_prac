import copy
f = open("./input.txt", 'r')

N,K=map(int,f.readline().strip().split(' '))
p=[]
r=[[0]*(K+1) for i in range(N)]

for i in range(N):
    w,v=map(int,f.readline().strip().split(' '))
    p.append((w,v))
p=sorted(p)
for idx,(w,v) in enumerate(p):
    if idx!=0:
        r[idx][:]=copy.deepcopy(r[idx-1][:])
    for i in range(w,K+1):
        if idx==0:
            r[idx][i]=v
        else:
            if r[idx-1][i]<v+r[idx-1][i-w]:
                r[idx][i]=v+r[idx-1][i-w]
            else:
                r[idx][i]=r[idx-1][i]
print(r[-1][K])
