""" March 17, 2025
given a number, print the perfect squares up

example:
user = 3
print 1,4,9"""

a = int(input("enter a number: "))

for i in range (1,a+1):
    ans = i**2
    print(ans)