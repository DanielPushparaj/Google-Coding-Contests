for x in range(int(input())):
    n1=int(input())
    time=[]
    for i in range(n1):
        temp=list(map(int,input().split()))
        temp.append(i)
        time.append(temp)
    time.sort()
    j1s=0
    j1e=0
    c1s=0
    c1e=0
    flag1=0
    result=[0]*n1
    for i in range(n1):
        f11=0
        f12=0
        if (time[i][0]>=j1s and time[i][0]<j1e) or (time[i][1]>j1s and time[i][1]<=j1e):
            f11=1
        if (time[i][0]>=c1s and time[i][0]<c1e) or (time[i][1]>c1s and time[i][1]<=c1e):
            f12=1
        if f11==0:
            result[time[i][2]]='J'
            j1s=time[i][0]
            j1e=time[i][1]
        elif f12==0:
            result[time[i][2]]='C'
            c1s=time[i][0]
            c1e=time[i][1]
        else:
            flag1=1
            break
    if flag1==0:
        answer="".join(result)
        print("Case #%d: %s"%(x+1,answer))
    else:
        print("Case #%d: IMPOSSIBLE"%(x+1))
        
