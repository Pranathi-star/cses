if __name__ == "__main__":
    n = int(input())

    res = []
    def generateCode(idx, pattern):
        if idx == n-1:
            res.append(pattern)
            return

        generateCode(idx + 1, pattern + "0")
        generateCode(idx + 1, pattern + "1")
    
    generateCode(0, "")

    for i in res:
        print("0" + i)
    for i in res[::-1]:
        print("1" + i)

    
