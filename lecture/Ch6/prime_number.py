def seive(n):
    candidates = list(range(2, n+1))
    i = 0
    while i < len(candidates):
        j = i+1
        while j < len(candidates):
            print(i, j)
            if candidates[j] != candidates[i] and candidates[j] % candidates[i] == 0:
                print(j)
                candidates.pop(j)
            j+=1
        i += 1
        print(candidates)
    return candidates

print(seive(50))
# 2 3 4 5 6 7 8 9 10
# 2 3 5 7 9
# A B C D AA
#