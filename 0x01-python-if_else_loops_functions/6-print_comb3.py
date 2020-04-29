#!/usr/bin/python3
for comb1 in range(10):
    for comb2 in range(comb1 + 1, 10):
        if comb1 == 8 and comb2 == 9:
            print("{}{}".format(comb1, comb2))
        else:
            print("{}{}, ".format(comb1, comb2), end="")