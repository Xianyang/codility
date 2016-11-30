# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

def solution(A):
    # write your code in Python 2.7

    if len(A) <= 2:
        return 0

    A.sort()

    for i in range(2, len(A)):
        if A[i - 2] + A[i - 1] > A[i]:
            return 1

    return 0

    pass


print solution([1, 4, 6])
print solution([10, 2, 5, 1, 8, 20] )
print solution([1])