from collections import defaultdict

times = int(input())

for i in range(times):
    N, K = map(int, input().split())
    a = list(map(int, input().split()))

    absk = abs(K)
    groups = defaultdict(list)

    for x in a:
        groups[x % absk].append(x)

    total_ops = 0

    if K > 0:
        for r, values in groups.items():
            values.sort()
            last = -10**30 

            for value in values:
                if value > last:
                    t = 0
                else:
                    t = (last + 1 - value + K - 1) // K
                new_val = value + t * K
                last = new_val
                total_ops += t

    else:
        step = -K
        for r, values in groups.items():
            values.sort(reverse=True)
            last = 10**30 

            for value in values:
                if value < last:
                    t = 0
                else:
                    t = (value - (last - 1) + step - 1) // step
                new_val = value - t * step
                last = new_val
                total_ops += t

    print(total_ops)
