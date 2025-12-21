test_cases = int(input())

cubes = []

for i in range(test_cases):
    bruh = input()
    words = [list(word) for word in input().split()]
    cubes.append(words)

for cube in cubes:
    first, second = sorted(cube[0]), sorted(cube[1])
    if first == second:
        print('Yes')
    else:
        print('No')