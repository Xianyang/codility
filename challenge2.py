# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

def solution(A):
    # write your code in Python 2.7

    A = sorted(A)
    ball_count = len(A)
    minMove = ball_count

    for i in range(A[0], A[-1] - ball_count + 2):
        row = [j for j in range(i, i + ball_count)]
        if len(row) == 0:
            continue

        count = 0
        for position in A:
            if position in row:
                count += 1

        minMove = min(minMove, ball_count - count)


    return minMove

    pass

print solution([6, 4, 1, 7, 10])
print solution([6, 4, 1, 7, 10, 11, 12, 13, 100, 101, 102, 103, 104, 105, 106, 107])