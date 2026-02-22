times = int(input())

for t in range(times):
    n, h, k = map(int, input().split())
    a = list(map(int, input().split()))

    S = sum(a)

    c = (h - 1) // S
    T_full = c * (n + k)
    h_rem = h - c * S

    p = [0] * n
    p[0] = a[0]
    for i in range(1, n):
        p[i] = p[i-1] + a[i]

    ans = next(i+1 for i in range(n) if p[i] >= h_rem)
    mx = max(a)
    pos = a.index(mx)
    for i in range(pos):
        if p[i] - a[i] + mx >= h_rem:
            ans = min(ans, i + 1)
            break

    print(T_full + ans)
