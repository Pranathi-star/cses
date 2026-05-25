if __name__ == "__main__":
    [n, x] = [int(i) for i in input().split()]

    weights = [int(i) for i in input().split()]

    weights.sort()

    ptr1 = 0
    ptr2 = n - 1

    res = 0
    curr = 0

    while ptr2 >= ptr1:
        curr += weights[ptr2]

        if weights[ptr1] + curr <= x:
            curr += weights[ptr1]
            ptr1 += 1
        
        ptr2 -= 1
        res += 1
        curr = 0
    
    print(res)

