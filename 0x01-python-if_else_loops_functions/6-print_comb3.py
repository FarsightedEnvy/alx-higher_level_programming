#!/usr/bin/python3
for k in range(9):
    for s in range(k + 1, 10):
        if k * 10 + s < 89:
            print("{:d}{:d}".format(k, s), end=", ")
print("{:d}".format(89))

