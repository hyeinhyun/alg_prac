def rotation(key):
    M=len(key)
    keys=[]
    keys.append(key)
    for _ in range(3):
        temp=[[0]*M for i in range(M)]

        for i in range(M):
            for j in range(M):
                temp[j][M-i-1]=key[i][j]
        keys.append(temp)
        key=temp
    return keys
def solution(key, lock):
    keys=rotation(key)
    N=len(lock)
    M=len(key)
    answer = True

    for i in range(N):
        for j in range(N):
            #범위 (i,j)
            if i-M+1>=0 and j-M+1>=0:
                #범위 : i-M+1~j-M+1
                for k in keys:
                    for ii in range(i-M+1,i+1):
                        for jj in range(j-M+1,i+1):
                            if lock[ii][jj]==1 and key[ii][jj]==1:
                                break
                            if lock[ii][jj]==0 and key[ii][jj]==0:
                                break
                
                
    return answer
