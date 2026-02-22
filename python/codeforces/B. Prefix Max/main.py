times = int(input())
for i in range(times):
    numbers = int(input())
    array = [int(x) for x in input().split()]
    print(max(array) * numbers)