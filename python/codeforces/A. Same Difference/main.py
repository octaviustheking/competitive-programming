times = int(input())
for i in range(times):
    bruh = input()
    letters = (list(input()))[::-1]
    counter = 0
    for j in range(len(letters) - 1):
        if letters[1 + j] != letters[0]:
            counter += 1
    print(counter)