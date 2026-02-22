def can(x, A, B, cA, cB, fA):
    candidates = {0, x}

    max_k = (B + x) // cB
    min_k = B // cB

    for k in range(max_k, min_k - 1, -1):
        p = B + x - (k * cB - 1)
        if 0 <= p <= x:
            candidates.add(p)

    for p in candidates:
        totalA = A + p
        totalB = B + (x - p)
        exchanges = totalB // cB
        totalA += exchanges * cA
        if totalA < fA:
            return False

    return True


t = int(input())
for _ in range(t):
    A, B, cA, cB, fA = [int(x) for x in input().split()]

    low, high = 0, 10**18
    while low < high:
        mid = (low + high) // 2
        if can(mid, A, B, cA, cB, fA):
            high = mid
        else:
            low = mid + 1

    print(low)
