# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

def solution(A, K):
    # write your code in Python 2.7

    B = []

    if A is []:
        return A

    if K % len(A) == 0:
        return A

    for i in range(0, len(A)):
        if i < K:
            B.append(A[-(K - i)])
        else:
            B.append(A[i - K])

    return B

    pass

print solution([1, 2, 3, 4, 5], 100)