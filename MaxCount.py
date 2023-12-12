l=[9,7,5,8,7,7,5,8]
a=max(l,key=lambda x:l.count(x))
c=max(l,key=l.count)
print(a)
print('second type')
print(c)