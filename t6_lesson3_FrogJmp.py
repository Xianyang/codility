# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

def solution(A):
    # write your code in Python 2.7
    A = sorted(A)

    if len(A) == 0:
        return 1

    if A[0] != 1:
        return 1

    if A[-1] != len(A) + 1:
        return len(A) + 1

    for i in range(len(A) - 1):
        if A[i + 1] - A[i] != 1:
            return A[i] + 1

    return 0
    pass

