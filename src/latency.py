from threading import Thread
import requests
import time


class Latency(Thread):
    latency_list = []
    latency_avg = 0
    def __init__(self,target):
        self.latency = 0
        Thread.__init__(self)
        self.url = "http://"+target.host+":"+str(target.port)

    def run(self):
        while True:
            try:
                response = requests.get(self.url).elapsed.total_seconds()s -
                self.latency_list.append(response)
                print("Latency : {}".format(response))
                time.sleep(20)
            except (KeyboardInterrupt, SystemExit):
                self.latency_avg = sum(self.latency_list) / len(self.latency_list)
                print("Average latency = {}".format(self.latency_list))
                break

    