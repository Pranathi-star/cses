if __name__ == "__main__":
    t = int(input())

    for i in range(t):
        (x, y) = (int(i) for i in input().split())

        rowPeri, colPeri, corner = False, False, False
        targetSq = 1

        if x == y:
            corner = True
            targetSq = x
        elif x > y:
            rowPeri = True
            targetSq = x
        else:
            colPeri = True
            targetSq = y

        if targetSq == 1:
            print(1)
        else:
            largestVal = targetSq * targetSq

            inc, dec = False, False

            offset = abs(y - x) #offset from sq corner
            if rowPeri:
                if targetSq % 2:
                    inc = True
                    val = largestVal - (x - 1) - offset
                else:
                    dec = True
                    val = largestVal - (x - 1) + offset
            else:
                if targetSq % 2:
                    dec = True
                    val = largestVal - (y - 1) + offset
                else:
                    inc = True
                    val = largestVal - (y - 1) - offset
            print(val)

            

            



        

