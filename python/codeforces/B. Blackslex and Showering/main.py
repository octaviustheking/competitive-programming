times = int(input())

for i in range(times):
    bruh = int(input())
    numbers = [int(x) for x in input().split()]
    original = sum(abs(numbers[i] - numbers[i + 1]) for i in range(bruh - 1))

    best_gain = 0
    best_gain = max(best_gain, abs(numbers[0] - numbers[1]))
    best_gain = max(best_gain, abs(numbers[bruh - 1] - numbers[bruh - 2]))

    for j in range(1, bruh - 1):
        gain = abs(numbers[j] - numbers[j - 1]) + abs(numbers[j] - numbers[j + 1]) - abs(numbers[j+  1] - numbers[j - 1])
        best_gain = max(best_gain, gain) 
        
    print(original - best_gain)