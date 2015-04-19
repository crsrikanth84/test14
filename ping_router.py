import threading
import time
import sys
import os

# BELOW CODE SNIPPET WILL TAKE TWO INPUTS FORM THE USER AND TRY TO PING TO A ROUTER/HOST IP ADDRESS USING THREADS

myLock = threading.Lock()

def ping_router(num, ipaddr):
    start = time.time()

    if os.system("ping -w 20 -n %d %s" % (num, ipaddr)) == 0:
        print ("######### %s is up ##########" % ipaddr)
    else:
        print ("######### %s is DOWN ##########" % ipaddr)

    time_elapsed = time.time() - start
    myLock.acquire(True)
    print ("######### %s thread took" % ipaddr, time_elapsed, "seconds")
    print ("#########################  END OF THREAD  ###################################")
    myLock.release()



####################################################################################################
# SAMPLE CODE TO INVOKE ABOVE THREAD IS AS SHOWN BELOW:
#
# METHOD - 1
#ipaddr1 = '8.8.8.8'
#thread1 = threading.Thread( target = ping_router, kwargs=dict(num=5,ipaddr=ipaddr1))
#thread1.start()
#
# METHOD - 2
thread2 = threading.Thread( target = ping_router, kwargs=dict(num=5,ipaddr='8.8.4.4'))
thread2.start()
