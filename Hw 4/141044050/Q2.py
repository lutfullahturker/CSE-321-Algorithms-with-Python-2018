def dict(word,myDictionary):
    if word in myDictionary:
        return True
    return False


def reconstitute(corruptedText,myDictionary):
    i = 0
    myFlag = 0
    word = ''
    retVal = list()
    while i < len(corruptedText):
        word = word + corruptedText[i]
        if dict(word,myDictionary):
            retVal.append(word)
            word = ''
            myFlag = i
        if len(word) == (len(corruptedText)-myFlag-1):
            if len(corruptedText)- 1 != myFlag:
                if len(retVal) != 0:
                    word = retVal.pop()
                    i = myFlag
                else:
                    print('Some words are not in dictionary !')
        i = i + 1
    return retVal


def main():
    test = 'therewasbestoftheturkey'
    myDictionary = ['there', 'was', 'fine', 'good', 'nice', 'term', 'i', 'hate', 'algorithm', 'course', 'best', 'of',
                    'the', 'turkey']
    result = reconstitute(test, myDictionary)
    print('Test String is ->>')
    print(test, end='\n\n')
    print('Result array is -->>')
    print(result)
    print('Result in string -->>')
    for i in range(len(result)):
        print(result[i], end=' ')


if __name__ == "__main__":
    main()
