class A:
    def __init__(self,z):
        self.a=z
    @property
    def double(self):
        return self.a*2

q=A(3)
print(q.double)

