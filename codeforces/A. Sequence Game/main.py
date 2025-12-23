tests = int(input())

for i in range(tests):
    bruh = input()
    numbers = [int(x) for x in input().split()]
    goal = int(input())
    numbers.sort()
    if numbers[0] <= goal <= numbers[-1]:
        print("YES")
    else:
        print("NO")