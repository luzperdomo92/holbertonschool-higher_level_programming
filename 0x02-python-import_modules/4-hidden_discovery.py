#!/usr/bin/python3
if __name__ == "__main__":
    from hidden_4 import *
    for files in dir():
        if files[:2] != "__":
            print("{}".format(files)
