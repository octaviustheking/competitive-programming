times = int(input())
for i in range(times):
    bruh = input()
    numbers = [int(x) for x in input().split()]
    numbers.sort()
    differences = [x - numbers[0] for x in numbers]
    if numbers[0] > differences[1]:
        print(numbers[0])
    else:
        print(differences[1])
