if __name__ == "__main__":
    s = input().strip()
    n = len(s)
    res = set()

    def allPerms(curr, all, idx, freq):
        if idx == n:
            res.add(curr)
            return

        for i in range(0, n):
            if freq[all[i]] > 0:
                if i > 0 and all[i] == all[i - 1]:
                    continue
                curr = curr + all[i]
                freq[all[i]] -= 1
                allPerms(curr, all, idx + 1, freq)
                curr = curr[:-1]
                freq[all[i]] += 1
        
    freq = {}
    for i in s:
        if i not in freq:
            freq[i] = 0
        freq[i] += 1

    allPerms("", s, 0, freq)

    print(len(res))

    if len(res) != 1:
        res = sorted(list(res))

    for i in res:
        print(i)
    