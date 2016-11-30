# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

def solution(S):
    # write your code in Python 2.7

    a = 0
    b = 0
    celebrate = 0

    for i in range(0, len(S)):
        win = S[i]
        if win is 'A':
            a += 1
        else:
            b += 1

        if a - b == 1:
            celebrate += 1

    return celebrate


    pass


print solution('ABBAAA')
print solution('BABBAA')