#evenorodd.py

# Ask the user for a number. 
# Depending on whether the number is even or odd, 
# print out an appropriate message to the user.

num = int(input('Enter a number: '))

if num % 2 == 0:
    print(str(num) + ' is an even number.')
elif num % 2 > 0:
    print(str(num) + ' is an odd number.')