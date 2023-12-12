from threading import Thread,Lock
class Hotel:
    def __init__(self,m):
        self.m=m
        self.l=Lock()
    def food(self):
        self.l.acquire()
        for i in range(1,6):
            print(self.m,i)
        self.l.release()
h1=Hotel('take order from tabel')
h2=Hotel('serve order to tabel')

t1=Thread(target=h1.food)
t2=Thread(target=h2.food)
t1.start()
t2.start()









