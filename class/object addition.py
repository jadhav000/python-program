class A:
    def __init__(self,m):
        self.m=m
    def __add__(self, other):
        return self.m+other.m

class B:
    def __init__(self,m):
        self.m=m



class C:
    def __init__(self,m):
        self.m=m
        print('in C',m)


a=A(11)
b=B(22)


print(a+b)