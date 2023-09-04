#Exercise #2
#Display total count of Even and Odd numbers

data = [24, 3, 60, 7, 9, 11]

even = 0
odd = 0

for num in data:
    if num % 2 == 0: # checks if even number (24 % 2 == 0), true = even
        even += 1
    else:
        odd += 1

print("Total even number: "+ str(even))
print("Total odd numbers: "+ str(odd))


