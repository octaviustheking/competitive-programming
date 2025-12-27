times = int(input())
for i in range(times):
    string = input()
    double_u = False
    if "uu" in string: double_u = True
    chars = list(string)

    if chars[0] == "s" and chars[-1] == "s" and not double_u:
        print("0")
    else:
        total_u = string.count("u")
        can_keep = [i for i in range(1, len(chars) - 1) if chars[i] == 'u']
        kept = 0
        prev = -10 ** 9
        for j in can_keep:
            if j - prev > 1:
                kept += 1
                prev = j
        print(total_u - kept)