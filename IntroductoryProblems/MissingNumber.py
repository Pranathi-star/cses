if __name__ == "__main__":
    n = int(input())

    nums = [int(i) for i in input().split()]

    res = 0;

    for i in range(1, n + 1):
        res ^= i
    
    for i in range(n - 1):
        res ^= nums[i]

    print(res)

        


