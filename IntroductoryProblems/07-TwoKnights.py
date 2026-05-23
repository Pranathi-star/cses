if __name__ == "__main__":


    def isValid(x, y, k):
        if x < 0 or x >= k or y < 0 or y >= k:
            return False
        return True
    cache = {}
    knightMoves = ((-2, +1), (-1, +2), (+1, +2), (+2, +1), (-2, -1), (-1, -2), (+1, -2), (+2, -1))
    k = int(input())
    for s in range(1, k + 1):
        if s in cache:
            print(cache[s])
        else:
            allPositions = ((s ** 2) * (s ** 2 - 1)) // 2
            attackPositions = 4 * (s - 1) * (s - 2)
            res = allPositions - attackPositions
            cache[s] = res
            print(res)

        



