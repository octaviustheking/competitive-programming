times = int(input())
for i in range(times):
    bruh = input()
    binary = [int(x) for x in input().strip()]

    ones = binary.count(1)
    length = len(binary)

    if ones == 0:
        print(0)
        continue

    if length % 2 == 1 and ones % 2 == 1:
        print(-1)
        continue

    if ones % 2 == 0:
        indices = [i for i, v in enumerate(binary) if v == 1]
    else:
        indices = [i for i, v in enumerate(binary) if v == 0]

    print(len(indices))
    print(*[i + 1 for i in indices])
