times = int(input())
for i in range(times):
    bruh = input()
    numbers = [int(x) for x in input().split()]
    set_numbers = sorted(set(numbers))
    previous_number = set_numbers[0]
    length = 0
    max_length = 0
    for number in set_numbers:
        if number == previous_number + 1:
            length += 1
        else:
            if length > max_length:
                max_length = length
            length = 1
        previous_number = number
    if length > max_length:
        max_length = length
    print(max_length)
