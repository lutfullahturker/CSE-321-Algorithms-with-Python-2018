def patternControl(charCheck):
    if charCheck == 'A' or charCheck == 'a':
        return 'to'
    elif charCheck == 'B' or charCheck == 'b':
        return 'be'
    elif charCheck == 'C' or charCheck == 'c':
        return 'or'
    elif charCheck == 'D' or charCheck == 'd':
        return 'not'
    else:
        return ''


def isPatternValid(string, pattern):
    if len(string) == 0:
        if len(pattern) == 0:  # if string and pattern reach here return 0, Successful case
            return 0
        else:
            return -1
    if len(pattern) == 0:  # if string  has finished but pattern has not finished, return -1
        return -1
    patternPart = patternControl(pattern[0])
    size = len(patternPart)
    if size == 0:
        return -1  # Invalid pattern letter

    for i in range(0, size):
        if string[i] != patternPart[i]:   # if string doesn't match with pattern, return -1
            return -1
    return isPatternValid(string[size:], pattern[1:])  # recursive call for remaining pattern letters


def main():
    x = isPatternValid("tobeornotTObe".lower(), "ABCDAb")
    if x == 0:
        print("Given pattern is valid on a given string.")
    else:
        print("Given pattern is not valid on a given string.")


if __name__ == '__main__':
    main()

