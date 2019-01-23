def maxSpan(arr, l, m, h):
    sum = 0
    leftSum = -99999
    rightSum = -99999
    firstInd = m

    for i in range(m, l, -1):
        sum = sum + arr[i]
        if sum >= leftSum :
            leftSum = sum
            firstInd = i

    sum = 0
    secInd = m+1
    for i in range(m + 1, h+1):
        sum = sum + arr[i]
        if (sum > rightSum):
            rightSum = sum
            secInd = i

    return (firstInd,secInd,leftSum + rightSum)


def maxSubSetSum(arr, l, h):
    if (l == h):
        return (l,l,arr[l])

    m = (l + h) // 2
    maxLow = maxSubSetSum(arr, l, m)
    maxHigh = maxSubSetSum(arr, m + 1, h)
    maxSpanSum = maxSpan(arr, l, m, h)


    maximum = max(maxLow[2], maxHigh[2], maxSpanSum[2])
    if maximum == maxLow[2]:
        return maxLow
    elif maximum == maxHigh[2]:
        return maxHigh
    elif maximum == maxSpanSum[2]:
        return maxSpanSum

    return maxLow


def main():
    arr = [-34, -5, 2, 5, 8, -20, 14, 36, -26, 28]
    size = len(arr)
    maxSum = maxSubSetSum(arr, 0, size - 1)

    print("Test Array is ->>")
    print(arr)
    print()
    print("Largest sum of contiguous subset is ", maxSum[2])
    print("Contiguous subset is -> ")
    print(arr[maxSum[0]:maxSum[1]+1])


if __name__ == '__main__':
    main()

