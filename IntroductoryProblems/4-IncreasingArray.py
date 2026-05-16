if __name__ == "__main__":
    n = int(input())
    arr = [int(i) for i in input().split()]
    res = 0

    for i in range(1, n):
        if arr[i] < arr[i - 1]:
            diff = (arr[i - 1] - arr[i])
            arr[i] += diff
            res += diff

    print(res)
