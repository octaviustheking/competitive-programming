from functools import lru_cache
import sys
sys.setrecursionlimit(10000)

def bruteforce(arr):
    n = len(arr)
    if n == 1:
        return 0, ()

    @lru_cache(maxsize=None)
    def dfs(state):
        L = len(state)
        if L == 1:
            return 0, ()
        new_state1 = state[1:]
        gain1, seq1 = dfs(new_state1)
        val1 = state[0] + gain1
        new_state2 = (state[0],) + state[2:]
        gain2, seq2 = dfs(new_state2)
        val2 = -state[1] + gain2

        if val1 >= val2:
            return val1, (0,) + seq1
        else:
            return val2, (1,) + seq2

    state0 = tuple(arr)
    return dfs(state0)

def read_int():
    line = input().strip()
    while line == "":
        line = input().strip()
    return int(line)

def read_n_ints(numbers):
    res = []
    while len(res) < numbers:
        parts = input().strip().split()
        if not parts:
            continue
        res.extend(map(int, parts))
    return res

times = read_int()
for i in range(times):
    n = read_int()
    arr = read_n_ints(n)
    best_value, best_seq = bruteforce(arr)
    print(best_value)
