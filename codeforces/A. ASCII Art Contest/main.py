scores = [int(x) for x in input().split()]
scores.sort()
if scores[2] - scores[0] >= 10:
    print("check again")
else:
    print("final " + str(scores[1]))