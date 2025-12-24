times = int(input())
for i in range(times):
    numbers = [int(x) for x in input().split()]
    if len(set(numbers)) == 1: print("YES")
    else: print("NO")