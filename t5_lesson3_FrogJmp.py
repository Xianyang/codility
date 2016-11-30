# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

def solution(X, Y, D):
    # write your code in Python 2.7
    if (Y - X) % D == 0:
        return (Y - X) / D
    else:
        return (Y - X) / D + 1
    pass

import math
def solution1(X, Y, D):
    # write your code in Python 2.7
    return int(math.ceil(float(Y - X) / D))
    pass

print solution1(2, 11, 3)