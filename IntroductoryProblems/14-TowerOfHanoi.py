if __name__ == "__main__":
    n = int(input())
    def towerOfHanoi(source, target, aux, num):
        if num == 1:
            return
        
        towerOfHanoi(source, aux, target, num - 1)
        print(source, aux)
        towerOfHanoi(source, target, aux, 1)
        print(source, target)
        towerOfHanoi(aux, target, source, num - 1)
        print(aux, target)

    towerOfHanoi(1, 3, 2, n)



