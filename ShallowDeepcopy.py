import copy

l=[[1,2],[3,4]]
a=copy.copy(l)
b=copy.deepcopy(l)
l[0][1]=0
print('a : ',a)
print('b : ',b)