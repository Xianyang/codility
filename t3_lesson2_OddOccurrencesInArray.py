# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

def solution(A):
    # write your code in Python 2.7

    A = sorted(A)

    i = 0
    while i < len(A):
        if i == len(A) - 1:
            return A[i]

        if A[i] == A[i + 1]:
            i = i + 2
        else:
            return A[i]
    pass

print solution([9, 3, 9, 3, 9, 7, 9, 7, 10, 10, 0, 0, 0, 0, 200])