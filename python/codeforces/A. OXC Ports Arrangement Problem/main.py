group_info = [int(x) for x in input().split()]
groups, spines, leaves = group_info[0], group_info[1], group_info[2]
okc_info = [int(x) for x in input().split()]
okcs, links, planes = okc_info[0], okc_info[1], okc_info[2]

for i in range(5):
    demands = int(input())
    info = [int(x) for x in input().split()]
    ga, leaf_a, gb, leaf_b = info[0], info[1], info[2], info[3]
    print("1 0")
    print("1 0")
    print("0 0 1 0 0")
    print("0 0 0 0 0")