if __name__ == "__main__":
    n = int(input())

    def generateCodes(idx, code, size):
        if idx == n:
            return code

        newCode = []
        for i in range(0, size):
            newCode.append("0" + code[i])
        
        for i in range(size - 1, -1, -1):
            newCode.append("1" + code[i])
        
        return generateCodes(idx + 1, newCode[::], len(newCode))
    
    code = ["00", "01", "11", "10"]
    if n == 1:
        print("0")
        print("1")
    elif n == 2:
        for i in code:
            print(i)
    else:
        res = generateCodes(2, code, 4)
        for i in res:
            print(i)


        




    
