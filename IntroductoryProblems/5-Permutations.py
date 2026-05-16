if __name__ == "__main__":
    n = int(input())

    if n == 1:
        print("1")
    elif n <= 3:
        print("NO SOLUTION")
    else:
        part1 = [str(i) for i in range(2, n + 1, 2)]

        part2 = [str(i) for i in range(1, n + 1, 2)]

        print(*part1, *part2)
            
            
            