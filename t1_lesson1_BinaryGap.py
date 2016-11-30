# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

def solution(N):
    # write your code in Python 2.7

    binary = bin(N)
    binary = binary[2:len(binary)]

    # step 1 delete 2^0, 2^1, 2^2,,,
    subString1 = binary[1:len(binary)]
    if '1' not in subString1:
        return 0

    # step 2 delete all 1
    if '0' not in binary:
        return 0

    # step 3
    arrayfor1 = []
    for i, c in enumerate(binary):
        if c is '1':
            arrayfor1.append(i)

    if len(arrayfor1) == 1:
        return 0

    array_for_length = []
    for i in range(1, len(arrayfor1)):
        length = arrayfor1[i] - arrayfor1[i - 1] - 1
        array_for_length.append(length)


    return max(array_for_length)

    pass

print solution(6)
print solution(529)
print solution(9)
print solution(20)