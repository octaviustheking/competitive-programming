from math import gcd
dimensions = [int(x) for x in input().split()]
pieces = int(input())

dimension_1 = gcd(dimensions[0], pieces)
pieces //= dimension_1

dimension_2 = gcd(dimensions[1], pieces)
dimension_3 = pieces // dimension_2

print(dimension_1, dimension_2, dimension_3)