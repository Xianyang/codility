# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

# FrogRiverOne

def solution(X, A):
    # write your code in Python 2.7

    if X > len(A) or X > max(A):
        return -1

    max_value = max(A)
    count = [0] * (X + 1)
    sum = 0

    for i in xrange(len(A)):

        if A[i] > X:
            continue

        if count[A[i]] == 1:
            continue

        count[A[i]] = 1
        sum += 1

        if sum == X:
            return i

    return -1

    pass

print solution(2, [1, 3, 1, 4, 2, 3, 5, 4])