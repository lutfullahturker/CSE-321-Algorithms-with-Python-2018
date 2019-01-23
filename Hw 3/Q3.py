
def binSearch(arr, low, high):
    if high >= low:
        mid =(low + high) // 2
        if mid == arr[mid]:
            return mid
        if mid > arr[mid]:
            return binSearch(arr, (mid + 1), high)
        else:
            return binSearch(arr, low, (mid-1))
    return -1


def main():
    arr = [-384, -5, 2, 5, 8, 10, 14, 16, 26, 786]
    print("Array =>")
    print(arr)
    print()
    size = len(arr)
    result = binSearch(arr, 0, size - 1)
    if result == -1:
        print("There is not an index i for which Arr[i] = i .")
    else:
        print("There is an index i for which Arr[i] = i .\ni = " + str(result))


if __name__ == '__main__':
    main()
