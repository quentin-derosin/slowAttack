import sys
import argparse

parser = argparse.ArgumentParser(
    description="Slow and low attack tools by Quentin and Stan"
)
def printHelp():
    pass

def initParser():
    parser.add_argument("-a","--addr",default="127.0.0.1",type=str,help="Host to perform attack, default localhost")
    parser.add_argument("-p","--port",default=8080,type=int,help="Port of the server, default = 8080")
    parser.add_argument("-s","--sockets",default=1000,help="Max socket use",type=int)
def parsArg():
    initParser()
    if len(sys.argv) <= 1:
        parser.print_help()
    return parser.parse_args()


