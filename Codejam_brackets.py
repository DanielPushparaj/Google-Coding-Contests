for x in range(int(input())):
    a=input()
    res=""
    open_b=0
    close_b=0
    for i in a:
        if i == '0':
            if open_b != 0:
                res += ')'*open_b
                open_b=0
                res+=i
            else:
                res+=i
        elif int(i) > open_b:
            res += '('*(int(i)-open_b)
            open_b=int(i)
            res += i
        elif int(i) < open_b:
            res += ')'*(open_b-int(i))
            open_b=open_b-(open_b-int(i))
            res+=i
        elif i == res[-1]:
            res += i
    if open_b != 0:
        res += ')'*open_b
    print("Case #%d: %s"%(x+1,res))
        
