times = int(input())
for i in range(times):
    word = input()
    chars = list(word)
    if len(chars) <= 10:
        print(word)
    else:
        print(chars[0] + str(len(chars) - 2) + chars[-1])