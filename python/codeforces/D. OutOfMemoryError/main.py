times = int(input())
for i in range(times):
    bruh, operations, max_value = [int(x) for x in input().split()]
    numbers = [int(x) for x in input().split()]

    test_numbers = list(numbers)
    for j in range(operations):
        index, added = [int(x) for x in input().split()]
        index -= 1
        if test_numbers[index] + added > max_value:
            test_numbers = list(numbers)
        else:
            test_numbers[index] += added
    print(*test_numbers)
