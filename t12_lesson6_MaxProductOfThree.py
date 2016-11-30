# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

def solution(A):
    # write your code in Python 2.7

    A.sort()

    first = A[-1] * A[-2] * A[-3]
    second = A[0] * A[1] * A[-1]

    return max(first, second)

    pass

print solution([-10, -9, 0, 1, 99])