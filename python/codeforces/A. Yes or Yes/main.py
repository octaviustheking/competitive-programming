times = int(input())
for i in range(times):
    chars = list(input())
    yes = [c for c in chars if c == "Y"]
    if len(yes) == 0 or len(yes) == 1:
        print("YES")
    else:
        print("NO")