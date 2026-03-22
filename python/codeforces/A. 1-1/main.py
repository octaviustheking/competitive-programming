times = int(input())
for i in range(times):
    n = int(input())
    s = [int(c) for c in input()]

    ones = [i for i, x in enumerate(s) if x == 1]

    if not ones:
        print(0, 0)
        continue

    work = s.copy()
    changed = True
    while changed:
        changed = False
        for j in range(1, n - 1):
            if work[j] == 0 and work[j-1] == 1 and work[j+1] == 1:
                work[j] = 1
                changed = True
    max_val = sum(work)
    
    work2 = work.copy()
    changed = True
    while changed:
        changed = False
        for j in range(1, n - 1):
            if work2[j] == 1 and work2[j-1] == 1 and work2[j+1] == 1:
                work2[j] = 0
                changed = True
    min_val = sum(work2)

    print(min_val, max_val)