for x in range(int(input())):
    n=int(input())
    arr=[]
    sol=""
    flag=0
    count=0
    for i in range(n):
        s=input()
        arr.append(s)
        if len(s)>len(sol):
            sol=s
    for i in arr:
        if i[1:] in sol:
            count+=1
        else:
            print("Case #%d: *"%(x+1))
            flag=1
            break
    if flag==0:
        print("Case #%d: %s"%((x+1),sol[1:]))
    
