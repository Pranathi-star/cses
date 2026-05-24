class AppleDivision:
    def __init__(self, weights, n):
        self.weights = weights
        self.n = n
        self.total = sum(weights)
        self.best_diff = float('inf')

    def search(self, idx, current_sum):
        if idx == self.n:
            diff = abs(self.total - 2 * current_sum)
            if diff < self.best_diff:
                self.best_diff = diff
            return

        self.search(idx + 1, current_sum + self.weights[idx])
        self.search(idx + 1, current_sum)

    def solve(self):
        self.search(0, 0)
        return self.best_diff


def main():
    n = int(input().strip())
    arr = [int(i) for i in input().split()]
    solver = AppleDivision(arr, n)
    print(solver.solve())

main()