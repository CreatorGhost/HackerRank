#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the encryption function below.
def encryption(z):
    # First of all we need to remove any extra space in the string
    x=z
    s=[]
    for i in (x):
        if i!= " ":
            s.append(i)
    # Now in s we contain list of all string without space
    p=0
    r=int(math.sqrt(len(s)))    #finding row
    c=r+1
    if math.sqrt(len(s)) == math.ceil(math.sqrt(len(s))):
        r=math.ceil(math.sqrt(len(s)))
        c=r
        
    elif c*r < len(s):
        r=r+1
    k=[]
    a=[]
    #creating an array to store all characters
    for i in range(r):
        for j in range(c):
            try:
                k.append(s[p])
                p+=1
            except IndexError:
                break
        a.append(k)
        k=[]
    en=[]
    s="".join(en)
    c=len(a[-1])    #Finding the last list size becouse it the only list that may varry in size
    t=[]
    for i in range(len(a[0])):
        for j in a:
            if j == a[-1]:
                if c!=0:
                    en.append(j[i])
                    c=c-1
            else:
                en.append(j[i])
        en.append(" ")
    ans="".join(en)
    return ans




if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = encryption(s)

    fptr.write(result + '\n')

    fptr.close()
