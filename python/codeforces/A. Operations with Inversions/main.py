# times = int(input())
# for i in range(times):
#     bruh = input()
#     array = [int(x) for x in input().split()]
#

n = 0
for i in range(5):
    z = 10 - i
    a = str(1089 * i)
    s = ""
    for j in range(len(a)):
        s = a[j] + s
    if s == str(1089 * z):
        n = n + 1
print(n)