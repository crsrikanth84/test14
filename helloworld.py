import threading
import time
import sys
import os


myLock = threading.Lock()

def ping_router(num, ipaddr):
    global var1
    start = time.time()
    while var1:
        time.sleep(2)
        if os.system("ping -w 20 -n %s %s" % (num, ipaddr)) == 0:
            time_elapsed = time.time() - start
            myLock.acquire(True)
            print ("######### %s is up ##########" % ipaddr)
            print ("######### %s thread took" % ipaddr, time_elapsed, "seconds")
            print ("#########################  END OF THREAD  ###################################")
            myLock.release()
        #elapsed_time = time.time() - start
        #print ("Time elapsed = ", elapsed_time, "\n######  Hit Enter to exit  ######\n" )

global var1
var1 = True
ipaddr1 = '8.8.8.8'
thread1 = threading.Thread( target = ping_router, kwargs=dict(num=5,ipaddr=ipaddr1))
thread1.start()

thread2 = threading.Thread( target = ping_router, kwargs=dict(num=5,ipaddr='8.8.4.4'))
thread2.start()

input('Hit Enter to exit')
var1 = False
print ("------------- Value of var1 in main = ", var1, "----------------")
