'''
Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each digit
of the number is an even number.
The numbers obtained should be printed in a comma-separated sequence on a single line.
'''

my_num = []

# for i in range(1000, 3001):
#     for j in str(i):
#         if int(j) in [2, 4, 6, 8]:
#             num.append(j)
#             if len(num) == 4:
#                 my_num.append(i)
#                 num.clear()

for i in range(1000, 3001):
    if all(int(j) % 2 == 0 for j in str(i)):
        my_num.append(str(i))

print(my_num)
