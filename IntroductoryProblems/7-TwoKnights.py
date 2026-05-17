if __name__ == "__main__":


    def isValid(x, y, k):
        if x < 0 or x >= k or y < 0 or y >= k:
            return False
        return True
    
    cache = {}
    knightMoves = ((-2, +1), (-1, +2), (+1, +2), (+2, +1), (-2, -1), (-1, -2), (+1, -2), (+2, -1))
    k = int(input())
    for s in range(1, k + 1):
        allPositions = ((s ** 2) * (s ** 2 - 1)) // 2
        attackPositions = 0

        if (s >= 3):
            if s in cache:
                print(cache[s])
            else:
                picked = set()
                for i in range(s):
                    for j in range(s):
                        for x in knightMoves:
                            new_x = i + x[0]
                            new_y = j + x[1]
                            if (i, j, new_x, new_y) not in picked and isValid(new_x, new_y, s):
                                attackPositions += 1
                                picked.add((i, j, new_x, new_y))
                    
                res = allPositions - (attackPositions // 2)
                cache[s] = res
                print(res)

        



