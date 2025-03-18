""" March 17, 2025
given a number, print multiplcation table up to 10

example:
user = 2
print 2,4,6,8,10,12...20"""

a = int(input("Enter a number: "))

for i in range(1,10+1):
    ans = i * a
    print(ans)