test_cases = int(input())
legs = []

for i in range(test_cases):
    legs.append(int(input()))

for leg in legs:
    if leg % 2 == 1:
        print("0")
    else:
        print(int(leg/4 + 1))