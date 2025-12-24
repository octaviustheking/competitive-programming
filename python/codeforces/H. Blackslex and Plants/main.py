# timed out, might try this in java.

times = int(input())
for i in range(times):
    stats = [int(x) for x in input().split()]
    plants = stats[0]
    water_ops = stats[1]
    total_water = [0] * plants
    for j in range(water_ops):
        bounds = [int(x) for x in input().split()]
        l = bounds[0]
        r = bounds[1]
        for k in range(l, r + 1):
            number = k - l + 1
            total_water[k-1] += number * (number & -number)
    print(*total_water)