if __name__ == "__main__":
    n = int(input())

    sum = (n * (n + 1)) // 2

    if (sum % 2):
        print("NO")
    else:
        reqSumPerSet = sum // 2

        nums = list(range(1, n + 1))
        
        set1 = set()
        currSum1 = reqSumPerSet

        for i in range(n - 1, -1, -1):
            if (nums[i] != -1 and currSum1 - nums[i] >= 0):
                set1.add(nums[i])
                currSum1 -= nums[i]
                nums[i] = -1
        
        set2 = set()
        currSum2 = reqSumPerSet

        for i in range(n - 1, -1, -1):
            if (nums[i] != -1 and currSum2 - nums[i] >= 0):
                set2.add(nums[i])
                currSum2 -= nums[i]
                nums[i] = -1

        if (currSum1 == 0 and currSum2 == 0):
            print("YES")
            print(len(set1))
            print(*set1)
            print(len(set2))
            print(*set2)
        else:
            print("NO")
            

        

