from threading import Thread
from time import sleep
def mr_slow(num1,num2):
    sleep(30)
    return num1/num2

a = mr_slow(1,2)
t = Thread(target=mr_slow, args= (1,2))
t.start()

print("hello world this is threading ")