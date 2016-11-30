# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

# PermCheck

def counting(A, m):
    n = len(A)
    count = [0] * (m) # A is from 1 to m
    for i in range(n):
        count[A[i] - 1] += 1
    return count


def solution(A):
    # write your code in Python 2.7

    if min(A) <= 0:
        return 0

    # get the max value
    max_value = max(A)

    if max_value > len(A):
        return 0

    count = counting(A, max_value)
    for value in count:
        if value != 1:
            return 0

    return 1

    pass

print solution([4, 1, 3, 2])
print solution([4, 1, 3, 2, 5, 7])
print solution([1, 1])
print solution([1000000000])