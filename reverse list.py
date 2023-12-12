l=[1,4,2,5,3]
n=len(l)
m=int(n/2)

for i in range(m):
    l[i],l[n-i-1]=l[n-i-1],l[i]
print(l)
