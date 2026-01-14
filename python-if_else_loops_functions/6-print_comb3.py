#!/usr/bin/python3
for r12 in range(10):
    for t5 in range(r12 + 1, 10):
        print("{:d}{:d}".format(r12, t5),
              end=", " if (t5 < 9 or r12 < 8) else "\n")
