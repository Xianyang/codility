
def solution(A):
    count = len(A)

    results = []

    for i in range(0, count):
        if i == 0:
            if sum(A) - A[i] == 0:
                return i


        elif i == count - 1:
            if sum(A) - A[i] == 0:
                return i

        else:
            sum1 = sum(A[0:i])
            sum2 = sum(A[i + 1: count + 1])
            if sum1 == sum2:
                return i

    return -1

array = [-1, 3, -4, 5, 1, -6, 2, 1]
print solution(array)