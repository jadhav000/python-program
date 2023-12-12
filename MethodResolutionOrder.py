class A:
    def __init__(self):
        print('This is A constructor')
class B(A):
    def __init__(self):
        super().__init__()
        print('This is B constructor')
class C(A):
    def __init__(self):
        super().__init__()
        print('This is C constructor')
class D(B,C):
    def __init__(self):
        super().__init__()
        print('This is D constructor')
d=D()
