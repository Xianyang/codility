# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

def solution(A):
    # write your code in Python 2.7

    if len(A) == 0:
        return 0

    A.sort()
    count = 1
    for i in xrange(1, len(A)):
        if A[i] != A[i - 1]:
            count += 1

    return count

    pass


print solution([1, 2, 3])
