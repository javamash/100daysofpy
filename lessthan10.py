#lessthan10.py

# take a list and write a program that prints elements less than 5

original_list = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

new_list = []

for i in original_list:
    if i < 5:
        new_list.append(i)
        
print(new_list)