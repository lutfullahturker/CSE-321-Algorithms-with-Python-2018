def mergeAndSort(matrix, arr):
    if len(matrix) == 0:
        return arr

    retVal = merge(matrix[0], arr)
    return mergeAndSort(matrix[1:], retVal)


def merge(L, R):
    arr = []
    i = 0  # L nin index i
    j = 0  # R nin index i

    while i < len(L) and j < len(R):
        if L[i] <= R[j]:
            arr.append(L[i])
            i += 1
        else:
            arr.append(R[j])
            j += 1

    while i < len(L):
        arr.append(L[i])
        i += 1

    while j < len(R):
        arr.append(R[j])
        j += 1
    return arr


def main():
    matrix = [[1, 6, 7],
              [2, 3, 5],
              [0, 9, 10],
              [4, 5, 8]]
    sortedArr = mergeAndSort(matrix, [])

    print("k sorted array =>> one dimentional sorted array ==>>")
    for i in range(0, len(sortedArr)):
        print(sortedArr[i], end=", ")


if __name__ == '__main__':
    main()
