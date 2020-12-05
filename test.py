a=[1,2,3]

b={1:[11,12],2:[22,23],3:[100]}
cand=[]
for i in a:
    if len(cand)==0:
        for kkk in b[i]:
            cand.append([kkk])
    else:
        temp=[]
        for kk in cand:
            for k in b[i]:
                print(kk)
                print(k)
                temp.append(kk+[k])
        print(temp)
        cand=temp
            