def pr(n):
    for i in range(2,n):
        if n%i==0 :
            break
    else:
        return n

l=list(filter(pr,range(5,15)))
print(l)