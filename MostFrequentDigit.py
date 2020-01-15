'''
finds the maximun occuring number in an array
'''

a=[int(x) for x in input().split()]
c=1
ma=0
d={}
for i in range (len(a)):
    if a[i] in d:
        c=d[a[i]]+1
        
        d[a[i]]=d[a[i]]+1
    if a[i] not in d:
        c=1
        d[a[i]]=c
    if ma < c:
        ma = c
        e=a[i]
print("elment that came max is: ",e," It came ",ma)
