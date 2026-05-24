if __name__ == "__main__":
    n = int(input().strip())

    nums = [int(i) for i in input().split()]

    nums.sort()
    res = 0

    for i in range(n):
        if ((i == 0) or (i > 0 and nums[i] != nums[i - 1])):
            res += 1
    
    print(res)

