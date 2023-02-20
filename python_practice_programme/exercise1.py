
# First exercise

'''
Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
between 2000 and 3200 (both included).
The numbers obtained should be printed in a comma-separated sequence on a single line.
Consider use range(#begin, #end) method
'''


r1 = []

for i in range(1999, 3200):
    if i % 7 == 0:
        r1.append(str(i))

result = ",".join(r1)

print('Following list contain all numbers which is divided by 7')
print(result)
