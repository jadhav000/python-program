from threading import *
from time import sleep
def light():
    sleep(3)
    e.set()
    print('Green light')
    sleep(5)
    print('red light')
    e.clear()

def traffic():
    e.wait()
    while e.isSet():

        print('you can go....')
        sleep(1)

e=Event()
t1=Thread(target=light)
t2=Thread(target=traffic)
t1.start()
t2.start()