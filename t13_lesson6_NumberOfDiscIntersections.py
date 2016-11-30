# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"
import itertools

def solution(A):
    if len(A) < 2:
        return 0

    left_edge = []
    right_edge = []

    for index, radius in enumerate(A):
        left_edge.append(index - radius)
        right_edge.append(index + radius)

    left_edge.sort()
    right_edge.sort()

    j = 0
    counter = 0

    for i in range(len(A)):
        while j < len(A) and right_edge[i] >= left_edge[j]:
            counter += j - i
            j += 1

        if counter > 10000000:
            return -1

    return counter

    pass


print solution([1, 5, 2, 1, 4, 0])