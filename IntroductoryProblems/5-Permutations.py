if __name__ == "__main__":
    n = int(input())

    if n == 1:
        print("1")
    elif n <= 3:
        print("NO SOLUTION")
    else:
        if n == 4:
            print("2 4 1 3")
        else:
            res = ""

            for i in range(1, n + 1, 2):
                res += (str(i) + " ")

            for i in range(2, n + 1, 2):
                res += (str(i) + " ")
            
            print(res[:-1])

            
            
            