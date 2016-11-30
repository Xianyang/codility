# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

def solution(A):
    # write your code in Python 2.7

    if len(A) == 0:
        return 0
    if len(A) == 1:
        return A[0]

    left = A[0]
    right = sum(A) - left
    result = abs(left - right)

    for i in range(1, len(A) - 1):

        left += A[i]
        right -= A[i]

        result = min(result, abs(left - right))

    return result
    pass

print solution([3, 1, 2, 4, 3])
print solution([])