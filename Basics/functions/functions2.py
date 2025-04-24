"""
In the wikipedia article above, you can see that it is a 3-place cipher
So A - 3 = X, B - 3 = Y, etc

Use the ord method to get the ascii representation of the letter ‘A’
Like in the computer ‘A’ -> 65, ‘B’ -> 66 and so on. Think of how you could use this instead of creating a large dict with the mapping of A -> X, B -> Y etc

Your cipher encoder and decoder must take input of string to encode/decode and the cipher skip key. 
Eg: 
str = “HELLO"
skip_key = 1

Result: GDKKN"""

"""ORD method
print(ord('A')) # Output: 65
print(ord('a')) # Output: 97
print(ord('Z')) # Output: 90
print(ord('z')) # Output: 122
print(chr(65))  # Output: 'A' """

"""str = "HELLO"
skip_key = 1"""

str = str(input("Enter a word: "))
skip_key = int(input("Enter how many keys to skip: "))
result = ""
for char in str:
    ord_method = ord(char) - skip_key
    result += chr(ord_method)
print(result)
