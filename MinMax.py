l=[9,2,6,4,1,3]
m=l[0]
n=l[0]
for i in l:
    if m<i:
        m=i
    if n>i:
        n=i
print('max : ',m)
print('min : ',n)