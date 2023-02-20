'''
Please write a program which counts and print the numbers of each character in a string input by console.
Example:
If the following string is given as input to the program:
abcdefgabc
Then, the output of the program should be:
a,2
c,2
b,2
e,1
d,1
g,1
f,1
Use dict to store key/value pairs.
Use dict.get() method to lookup a key with a default value.
'''


dic = {}
s = input('Enter your value =')
for i in s:
    dic[i] = dic.get(i,0)+1

x = '\n'.join(['%s,%s' % (k, v) for k, v in dic.items()])
print(x)
# for keys, values in dic.items():
#     result = ','.join([keys, values])
#     print(result)