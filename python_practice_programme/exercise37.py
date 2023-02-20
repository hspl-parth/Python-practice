'''
Write a program to solve a classic ancient Chinese puzzle:
We count 35 heads and 94 legs among the chickens and rabbits in a farm. How many rabbits and how many
chickens do we have?
'''

# chickens = 0
# rabbits = 0


# def AnimalCount(h, l):
#     if h > l:
#         print('That is not possible')
#     elif l % 2 != 0:
#         print('That is not possible')
#     else:


def solve(numheads, numlegs):
    ns = 'No solution'
    for i in range(numheads + 1):
        j = numheads - i
        if 2*i+4*j == numlegs:
            return i,j
    return ns

result = solve(35, 94)
print(result)