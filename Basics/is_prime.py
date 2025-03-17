""" March 16, 2025

take input of a number
output if its prime or not
prime number: a whole number greater than 1 that cannot be exactly divided by any whole number other than itself and 1 (e.g. 2, 3, 5, 7, 11).

example:
17, prime
5, prime
10, composite"""

a = int(input("Please enter a number: "))

isprime = True
for i in range(2,a):
    if a % i == 0:
        isprime = False
        break

if isprime:
    print(f"{a} is prime.")
else:
    print(f"{a} is a composite.")