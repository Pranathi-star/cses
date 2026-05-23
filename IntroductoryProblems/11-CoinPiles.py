if __name__ == "__main__":
    t = int(input())

    for i in range(t):
        [n1, n2] = [int(i) for i in input().split()]
        larger = max(n1, n2)
        total = n1 +  n2
        if (total % 3 == 0 and larger <= (2 * (total - larger))):
            print("YES")
        else:
            print("NO")
