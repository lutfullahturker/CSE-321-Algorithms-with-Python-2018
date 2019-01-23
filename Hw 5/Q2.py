def findOptimumCost(n,m,nArr,sArr):
    optS = 0
    optN = 0

    for i in range(1, n):
        lastS = optS
        lastN = optN
        optN = nArr[i] + min(lastN,m+lastS)
        optS = sArr[i] + min(lastS,m+lastN)

    return min(optS,optN)


def main():
    # odev PDF'inde index ler 1 den baslayacak sekilde yazildigi icin indexler 1 den baslasin diye baslarina 0 koydum.
    nArr = [0, 1, 3, 20, 30] # aylara gore o ile ait cost lar (her eleman 1 ayin cost u)
    sArr = [0, 50, 20, 2, 4]
    n = 4  # ay sayisi
    m = 10 # sehir degistirme cost u

    optimumCost = findOptimumCost(n + 1,m,nArr,sArr)
    print("Example in Homework PDF file ->\nS ->", end="")
    print(sArr[1:])
    print("N ->", end="")
    print(nArr[1:])
    print(optimumCost)

    nArr = [0, 12, 18, 10, 12]
    sArr = [0, 18, 12, 15, 9]
    optimumCost = findOptimumCost(n + 1, m, nArr, sArr)
    print("\nExample in my Report PDF file ->\nS ->", end="")
    print(sArr[1:])
    print("N ->", end="")
    print(nArr[1:])
    print(optimumCost)


if __name__ == "__main__":
    main()
