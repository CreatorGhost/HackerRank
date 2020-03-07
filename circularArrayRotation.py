#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the circularArrayRotation function below.
def circularArrayRotation(a, k, queries):
    z=k%len(a)-1
    a=a[::-1]       #first reverse all array
    r1=a[z::-1]     #then reverse till k element
    r2=a[:z:-1]     #then reverse the remaning elements
    r2=r1+r2        #add them to form a rotated array
    l=[]
    for i in queries:
        l.append(r2[i])
    return l

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nkq = input().split()

    n = int(nkq[0])

    k = int(nkq[1])

    q = int(nkq[2])

    a = list(map(int, input().rstrip().split()))

    queries = []

    for _ in range(q):
        queries_item = int(input())
        queries.append(queries_item)

    result = circularArrayRotation(a, k, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
