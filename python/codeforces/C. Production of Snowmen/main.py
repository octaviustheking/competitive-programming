times = int(input())

def good_shift(x, y):
    x_length = len(x)
    good = [True] * x_length
    for j in range(x_length):
        ok = True
        for k in range(x_length):
            if x[k] >=y[(k + j) % x_length]:
                ok = False
                break
        good[j] = ok
    return good

for i in range(times):
    bruh = int(input())
    heads = [int(x) for x in input().split()]
    torsos = [int(x) for x in input().split()]
    bottoms = [int(x) for x in input().split()]
    goodht = good_shift(heads, torsos)
    goodtb = good_shift(torsos, bottoms)
    cht = sum(goodht)
    ctb = sum(goodtb)

    print(bruh * cht * ctb)
