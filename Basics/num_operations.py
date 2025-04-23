"""April 22, 2025

Input: 12345
Output: 1  // 1 digit
    2  // Digit next to 1st digit
    3
    4
    5  // Last Digit of the number 

The input cannot be converted into a string. 
You must extract the digits by doing math operations on the integer"""

"""a = int(input("Enter a number: "))"""

a = 123456789

len_a = len(str(a))


remainder = 0

for i in range (len_a-1,-1,-1):
    remainder = a // (10 ** i)
    print(remainder)
    a = a % (10 ** i)

