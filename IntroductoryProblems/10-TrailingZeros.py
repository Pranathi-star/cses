if __name__ == "__main__":
    n = int(input())
    curr = 1
    res = 0
    currPow = (5 ** curr)
    while (currPow <= n):
        res += (n // currPow)
        curr += 1
        currPow = (5 ** curr) 
    
    print(res)



