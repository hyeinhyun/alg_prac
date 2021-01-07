import copy
def rotation(key):
    keys=[key]
    for _ in range(3):
        temp=list(zip(*key[::-1]))
        keys.append(temp)

        key=temp
    return keys
def check(result):
    N=len(result)
    w=[[1]*N for i in range(N)]
    if result == w:
        return True
    return False
def solution(key, lock):
    keys=rotation(key)
    N=len(lock)
    M=len(key)-1
    answer = False
    for k in keys:
        for i in range(N+M+1):
            for j in range(N+M+1):
                print((i,j))
                lock_t=copy.deepcopy(lock)
                #겹치는 부분 변경 : 범위 : [i,i-1,...i-M][j,j-1,...,j-M]
                for idx_m,i_m in enumerate(range(i-M,i+1)):
                    if i_m>=0 and i_m<N:#do something
                        for jdx_m,j_m in enumerate(range(j-M,j+1)):
                            if j_m>=0 and j_m<N:
                                print(i_m,j_m)
                                lock_t[i_m][j_m]=lock[i_m][j_m]+k[idx_m][jdx_m]
                if check(lock_t):
                    return True


                
                
    return answer
print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]],[[1, 1, 1], [1, 1, 0], [1, 0, 1]]	))
