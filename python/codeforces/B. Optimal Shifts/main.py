times = int(input())
for i in range(times):
    bruh = input()
    nums = list(input())
    counter = 0
    max_counter = 0
    nums = nums + nums
    for num in nums:
        if num == "0":
            counter += 1
        else:
            max_counter = max(max_counter, counter)
            counter = 0
    print(max(max_counter, counter))