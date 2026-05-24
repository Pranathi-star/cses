if __name__ == "__main__":

    def game(p1, p2, scoreDist, nonZeroCnt):
        if len(res):
            return 
        if nonZeroCnt == 0:
            res.append((p1[::], p2[::]))
            return
        
        # case 1 -> p1 winning move

        if scoreDist[0] > 0:
            for i in range(1, n + 1):
                for j in range(1, i):
                    if i not in p1 and j not in p2:
                        p1.append(i)
                        p2.append(j)
                        scoredDist[0] -= 1
                        if scoredDist[0] == 0:
                            nonZeroCnt -= 1
                        game(p1, p2, scoredDist, nonZeroCnt)
                        p1.pop()
                        p2.pop()
                        scoredDist[0] += 1
                        if scoredDist[0] == 1:
                            nonZeroCnt += 1

        # case 2 -> p2 winning move

        if scoreDist[1] > 0:
            for i in range(1, n + 1):
                for j in range(i + 1, n + 1):
                    if i not in p1 and j not in p2:
                        p1.append(i)
                        p2.append(j)
                        scoredDist[1] -= 1
                        if scoredDist[1] == 0:
                            nonZeroCnt -= 1
                        game(p1, p2, scoredDist, nonZeroCnt)
                        p1.pop()
                        p2.pop()
                        scoredDist[1] += 1
                        if scoredDist[1] == 1:
                            nonZeroCnt += 1

        # case 3 -> draw

        if scoreDist[2] > 0:
            for k in range(1, n + 1):
                if k not in p1 and k not in p2:
                    p1.append(k)
                    p2.append(k)
                    scoredDist[2] -= 1
                    if scoredDist[2] == 0:
                        nonZeroCnt -= 1
                    game(p1, p2, scoredDist, nonZeroCnt)
                    p1.pop()
                    p2.pop()
                    scoredDist[2] += 1
                    if scoredDist[2] == 1:
                        nonZeroCnt += 1

    t = int(input().strip())

    for x in range(t):
        [n, a, b] = [int(i) for i in input().split()]

        scoredDist = [a, b, n - (a + b)]

        res = []

        nonZeroCnt = 0

        for i in scoredDist:
            if i > 0:
                nonZeroCnt += 1
        game([], [], scoredDist, nonZeroCnt)

        if len(res) == 0:
            print("NO")
        else:
            print("YES")
            print(*res[0][0])
            print(*res[0][1])

    
        

        