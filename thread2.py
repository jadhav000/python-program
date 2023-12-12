from threading import *

def disp():
    print('this is display')

t1=Thread(target=disp)

print(current_thread().name)
print(current_thread().daemon)