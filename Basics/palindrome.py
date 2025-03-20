""" March 19, 2025
palindrome example: madam and racecar

take user input of string
output is palindrome or not"""

import math

a = str(input("Enter a word: "))

""" indexing example:
s = "hello" 
len(s) = 5
s[0] is h
s[1] is e
s[2] is l
s[3] is l
s[4] is o, len-1"""

front = 0
back = len(a)-1
# middle = math.ceil(len(a)/2)
middle = len(a) // 2
palindrome = False
"""range(x,y,z)
x = starting number
y = ending number minus 1 
z = increment"""


for i in range (0,middle):

    if a[front] == a[back]:
        front += 1
        back -= 1
        palindrome = True

    else:
        palindrome = False
        break

print(palindrome)
print(middle)