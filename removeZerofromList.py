l=[1,2,0,0,3,0,2,0]
for i in l:
    if i==0:
        l.remove(i)
        l.append(i)
print(l)