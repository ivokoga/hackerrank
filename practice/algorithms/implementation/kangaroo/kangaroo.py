#!/bin/python3

import sys

def kangaroo(x1, v1, x2, v2):
    # Complete this function
    if x1 < x2:
        if v1 > v2:
            xdiff = abs(x1-x2)
            vdiff = abs(v1-v2)
            if(xdiff % vdiff ==0):
                return "YES"
            else:
                return "NO"
    return "NO"

x1, v1, x2, v2 = input().strip().split(' ')
x1, v1, x2, v2 = [int(x1), int(v1), int(x2), int(v2)]
result = kangaroo(x1, v1, x2, v2)
print(result)