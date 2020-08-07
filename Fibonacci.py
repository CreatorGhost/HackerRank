# Recursive Solution with O(2^n) Time Complexity and O(n) Space Complexity
'''
def getNthFib(n):
	if n == 1:	return 0
	if n == 2:	return 1
	
	
	return getNthFib(n-1)+getNthFib(n-2)
'''

# Recursive and Memoization Solution with O(n) Time Complexity and O(n) Space Complexity
'''
memoize={1:0,2:1}
def getNthFib(n):
	if n in memoize:   return memoize[n]
	else:   memoize[n]=getNthFib(n-1)+getNthFib(n-2)
	return memoize[n]

'''

# Iterative Solution with O(n) Time Complexity and O(1) Space Complexity
'''
def getNthFib(n):
    if n == 1:    return 0
    if n == 2:   return 1
    first,second=0,1
    for i in range(2,n):
        ans= first+second
        first= second
        second = ans
    return ans
'''
print(getNthFib(4))
