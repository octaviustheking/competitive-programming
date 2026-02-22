times = int(input())
for i in range(times):
    bruh = input()
    string = list(input())

    length = len(string)
    transitions = 0
    adj = False

    for j in range(length):
        if string[j] != string[(j + 1) % length]:
            transitions += 1
        else:
            adj = True
    if adj:
        print(transitions + 1)
    else:
        print(transitions)

