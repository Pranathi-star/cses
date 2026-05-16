if __name__ == "__main__":

    def getCharMaxLen(string, char):
        maxLen, currLen = 0, 0

        for i in string:
            if i == char:
                currLen += 1
            else:
                currLen = 0
    
            maxLen = max(maxLen, currLen)

        return maxLen

    string = input()

    res = 0

    chars = ["A", "C", "G", "T"]
    for char in chars:
        maxLenForChar = getCharMaxLen(string, char)

        res = max(maxLenForChar, res)

    print(res)