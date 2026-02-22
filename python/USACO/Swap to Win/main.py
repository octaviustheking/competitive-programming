from collections import defaultdict

times = int(input())
for i in range(times):
    N, M = map(int, input().split())
    t = list(input().rstrip())
    s = [list(input().rstrip()) for _ in range(N)]

    loc = defaultdict(set)
    for x in range(N):
        for k in range(M):
            loc[s[x][k]].add((x, k))

    ops = []

    def swap1(x, p, q):
        loc[s[x][p]].discard((x, p))
        loc[s[x][q]].discard((x, q))
        s[x][p], s[x][q] = s[x][q], s[x][p]
        loc[s[x][p]].add((x, p))
        loc[s[x][q]].add((x, q))

    def swap2(x, y, k):
        loc[s[x][k]].discard((x, k))
        loc[s[y][k]].discard((y, k))
        s[x][k], s[y][k] = s[y][k], s[x][k]
        loc[s[x][k]].add((x, k))
        loc[s[y][k]].add((y, k))

    for j in range(M):
        if s[0][j] == t[j]:
            continue

        need = t[j]

        found = False
        for q in range(j+1, M):
            if s[0][q] == need:
                ops.append(f"1 1 {j+1} {q+1}")
                swap1(0, j, q)
                found = True
                break

        if found:
            continue

        for (x, k) in loc[need]:
            if x == 0:
                continue
            if k != j:
                ops.append(f"1 {x+1} {j+1} {k+1}")
                swap1(x, j, k)
            ops.append(f"2 1 {x+1} {j+1}")
            swap2(0, x, j)
            break

    print(len(ops))
    for op in ops:
        print(op)