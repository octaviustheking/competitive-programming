import sys
from math import ceil
input = sys.stdin.readline

 
def solve():
    n, m, l = map(int, input().split())
    a = list(map(int, input().split()))
    gaps = []
    prev = 0
    for x in a:
        gaps.append(x - prev)
        prev = x
    gaps.append(l - prev)
    gaps.sort(reverse=True)
    print(ceil(gaps[n] / m))


t = int(input())
for _ in range(t):
    solve()