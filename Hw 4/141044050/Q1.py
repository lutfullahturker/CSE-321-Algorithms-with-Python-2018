
def fillOptimalList(opt, distanceArr):
    opt.append(0)
    for i in range(1, len(distanceArr)):
        minimum = 999999
        for j in range(0, i):
            equa = opt[j] + (200 - (distanceArr[i] - distanceArr[j]))**2
            if minimum > equa:
                minimum = equa
        opt.append(minimum)


def main():
    optimal = list()
    A = [0, 190, 220, 410, 580, 640, 770, 950, 1100, 1350]
    fillOptimalList(optimal, A)

    print("Optimal Sequance is ==>>")
    for i in range(0, len(optimal)):
        print(optimal[i], end=", ")


if __name__ == '__main__':
    main()
