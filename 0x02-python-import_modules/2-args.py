#!/usr/bin/python3
import sys
i = 1
print("{} arguments".format(len(sys.argv) - 1))
for arg in sys.argv[1:]:
    print("{}: {}".format(i, arg))
    i += 1