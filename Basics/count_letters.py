""" March 16, 2025
three double-quotes are for multiple lines comments"""

"""program to count frequency of each letter in a word
given the word 'hello' 
output should be h=1 e=1 l=2 o=1"""

user = str(input("Enter a word to count the frequency of each letter: "))



for i in user:
    count  = 0
    for j in user:
        if i == j:
            count += 1

    print (f"the occurance of {i} is {count}")
        

