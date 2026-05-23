if __name__ == "__main__":
    s = input().strip()

    oddCount = 0
    n = len(s)

    freq = {}

    for i in s:
        if i not in freq:
            freq[i] = 0
        freq[i] += 1
            
    for i in freq:
        if freq[i] % 2:
            oddCount += 1
    if (oddCount >= 1 and not n % 2) or (oddCount > 1 and n % 2):
        print("NO SOLUTION")
    else:
        res = [""] * n
        curr = 0

        for i in freq:
            for j in range(freq[i] // 2):
                res[curr] = i
                res[-1 - curr] = i
                curr += 1
            if freq[i] % 2:
                res[n // 2] = i
        
        print(''.join(res))
            




         
            
