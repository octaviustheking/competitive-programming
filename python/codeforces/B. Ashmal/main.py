times = int(input())

for i in range(times):
    bruh = input()
    strings = input().split()
    final_string = ""
    for string in strings:
        if (string + final_string) < (final_string + string):
            final_string = string + final_string
        else:
            final_string = final_string + string
    print(final_string)