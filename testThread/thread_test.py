import threading
import time
class thread_test(threading.Thread):
    def __init__(self,threadname):
        threading.Thread.__init__(self,name=threadname)
    def run(self):
        global number
        number=number+1
        time.sleep(1)
        print("the value of number is {}".format(number))

threadlist=[]
for i in range(5):
    t = thread_test(str(i))
    threadlist.append(t)
number=0
for i in threadlist:
    i.start()