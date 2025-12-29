times = int(input())

# ew a function
def can_make(mid, wc, bc):
    odd_layer = (mid + 1) // 2
    even_layer = mid // 2
    odd_sum = (4 ** odd_layer - 1) // 3
    even_sum = 2 * (4 ** even_layer - 1) // 3

    if (odd_sum <= wc and even_sum <= bc) or (odd_sum <= bc and even_sum <= wc):
        return True
    return False

for i in range(times):
    chocolates = [int(x) for x in input().split()]
    low, high = 0, 60
    while low < high:
        mid = (low + high + 1) // 2
        if can_make(mid, chocolates[0], chocolates[1]):
            low = mid
        else:
            high = mid - 1
    print(low)
