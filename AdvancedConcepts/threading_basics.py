import threading
import time


def myfunction():
    print ("Start a Thread")
    time.sleep(3)
    print ("End a Thread")


threads = []

for i in range(5):
    myfunction()
    th = threading.Thread(target=myfunction)
    th.start()
    threads.append(th)

for th in threads:
    th.join()
