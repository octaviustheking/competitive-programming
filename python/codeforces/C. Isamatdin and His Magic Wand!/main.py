lo_nums = []

for i in range(int(input())):
    bruh = input()
    working = [int(x) for x in input().split()]

    final_string = ""
    new_list = working

    if len({x & 1 for x in working}) == 2: new_list = sorted(working)

    # rmb this cuz it makes it faster
    final_string = " ".join(map(str, new_list))

    lo_nums.append(final_string.strip())

[print(x) for x in lo_nums]