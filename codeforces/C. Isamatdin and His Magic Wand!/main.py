lo_nums = []

for i in range(int(input())):
    bruh = input()
    working = [int(x) for x in input().split()]

    final_string = ""
    new_list = working

    if not (all(x % 2 == 0 for x in working) or all(x % 2 == 1 for x in working)): new_list = sorted(working)

    for x in new_list:
        final_string += (" " + str(x))

    lo_nums.append(final_string.strip())

[print(x) for x in lo_nums]