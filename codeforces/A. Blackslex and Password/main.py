times = int(input())

for i in range(times):
    nums = [int(x) for x in input().split()]
    print(nums[0] * nums[1] + 1)