class A:
    def qs(self):
        print('a')
class B(A):
    def qs(self):
        super().qs()
        print('b')
class C(A):
    def qs(self):
        super().qs()
        print('c')
class D(B,C):
    pass

d=D()
d.qs()