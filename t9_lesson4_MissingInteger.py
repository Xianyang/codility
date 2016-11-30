# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

# missing integer

def solution(A):
    # write your code in Python 2.7

    A = sorted(A)

    if A[-1] <= 0:
        return 1

    for i in xrange(len(A)):
        if A[i] == 1:
            sub_array = A[i:]
            break
        elif A[i] > 1:
            return 1

    max_value = min(max(sub_array), 100000)
    length = len(sub_array)
    count = [0] * max_value

    for i in range(length):
        if sub_array[i] > 100000:
            continue

        count[sub_array[i] - 1] = 1

    if 0 in count:
        return count.index(0) + 1
    else:
        return max_value + 1

    pass

# print solution([1, 3, 6, 4, 1, 2])
# print solution([-1, -2, 0, 2, 1, 100])
# print solution([0])
# print solution([1, 2])
# print solution([-2147483648, 2147483647])
print solution([1])
print solution([-10, -9, -2, -1])
print solution([-1, 1, -1, 1, -2, 2, 3, -2, 1, 2, 3, 0])