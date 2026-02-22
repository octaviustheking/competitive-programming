MOD = 10**9 + 7

T = int(input())
for _ in range(T):
    x = input().strip()
    steps = 0

    while x != "0":
        if all(c in '01' for c in x):
            s = list(x)
            i = len(s) - 1
            while i >= 0 and s[i] == '0':
                s[i] = '9'
                i -= 1
            if i >= 0:
                s[i] = chr(ord(s[i]) - 1)
            x = ''.join(s).lstrip('0')
            if x == "":
                x = "0"
            steps += 1
        else:
            y = []
            for c in x:
                y.append('1' if (ord(c) - 48) % 2 else '0')
            x = ''.join(y).lstrip('0')
            if x == "":
                x = "0"
            steps += 1

    print(steps % MOD)
