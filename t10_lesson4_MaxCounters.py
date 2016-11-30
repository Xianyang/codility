# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

def solution(N, A):
    # write your code in Python 2.7

    if min(A) == N + 1 and max(A) == N + 1:
        return [0] * N

    counters = [0] * N
    max_value = 0
    last_operation = None

    for index, operation in enumerate(A):
        if operation == N + 1:
            if operation == last_operation:
                if max(A[index:]) == N + 1 and min(A[index:]) == N + 1:
                    break
                continue

            counters = [max_value] * N
        else:
            counters[operation - 1] += 1
            if counters[operation - 1] > max_value:
                max_value = counters[operation - 1]

        last_operation = operation

    return counters

    pass


# print solution(5, [3, 4, 4, 6, 1, 4, 4])
print solution(5, [1, 6, 6, 6, 6, 6, 6, 6])