if __name__ == "__main__":
    n = int(input())

    moves = []
    def towerOfHanoi(source, target, aux, num):
        if num == 1:
            moves.append((source, target))
            return
        
        towerOfHanoi(source, aux, target, num - 1)

        towerOfHanoi(source, target, aux, 1)

        towerOfHanoi(aux, target, source, num - 1)


    towerOfHanoi(1, 3, 2, n)
    print(len(moves))
    for i in moves:
        print(i[0], i[1])



