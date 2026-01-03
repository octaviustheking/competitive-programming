import math
times = int(input())
for i in range(times):
    numbers = [int(x) for x in input().split()]
    l, a, b = numbers[0], numbers[1], numbers[2]
    d = math.gcd(b, l)
    c = a + d * ((l - 1 - a) // d)
    print(c)