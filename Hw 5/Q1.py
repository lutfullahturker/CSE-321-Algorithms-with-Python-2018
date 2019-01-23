def findOptimum(jobs):
    tmp = list()
    orderedArr = list()
    maxim = 0
    t = 0
    result = 0
    for i in range(len(jobs)):
        tmp.append(jobs[i][1] / jobs[i][0])
    flag = 0
    for j in range(0, len(jobs)):
        for k in range(len(jobs)):
            if tmp[k] > maxim:
                maxim = tmp[k]
                flag = k

        orderedArr.append(jobs[flag])
        t = t + orderedArr[j][0]
        result = result + (t * orderedArr[j][1])
        tmp[flag] = 0
        maxim = 0

    return orderedArr, result


def main():
    jobs = [(1, 10), (5, 2), (4, 8)]
    test, result = findOptimum(jobs)

    print("Optimum Order ->")
    print(test)
    print("Result -> ", end="")
    print(result)


if __name__ == "__main__":
    main()
