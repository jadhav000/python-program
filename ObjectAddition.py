class A:
    def __init__(self,a):
        self.a=a
        self.z=7

    def __add__(self, other):
        x=self.a+other.a
        self.z=A(x)
        return self.z
    def __str__(self):
        return str(self.z)
class B:
    def __init__(self,a):
        self.a=a
class C:
    def __init__(self,a):
        self.a=a
a=A(10)
b=A(10)
c=A(10)
v=a+b+c
print(v)
