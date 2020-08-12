#divisors.py

# ask the user for a number and list out all possible divisors

dividend = int(input('Enter a number to be divided: '))
divisors = []

for i in range(1, dividend):
    if dividend % i == 0:
        divisors.append(i)
        
print(divisors)