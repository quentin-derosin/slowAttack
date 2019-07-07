from threading import Thread
import requests
import time


class Latency(Thread):
    def __init__(self,target):
        self.latency = 0
        Thread.__init__(self)
        self.url = "http://"+target.host+":"+str(target.port)

    def run(self):
        while True:
            response = requests.get(self.url).elapsed.total_seconds()
            print("Latency : {}".format(response))
            time.sleep(20)

    