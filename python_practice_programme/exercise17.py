'''
Write a program that computes the net amount of a bank account based on a transaction log from console
input. The transaction log format is shown as follows:
D 100
W 200
D means deposit while W means withdrawal.
Suppose the following input is supplied to the program:
D 300
D 300
W 200
D 100
Then, the output should be:
500
'''

# digit_input = input('Enter the your sequence = ')
# digit = digit_input.split()

multiline = []
deposit = []
withdraw = []

while True:
    line = input('Enter your logs = ')
    if line:
        multiline.append(line)
    else:
        break
    digit = line.split()
    # deposit = []
    for i in range(len(digit)):
        if digit[i] == 'D':
            deposit.append(digit[i+1])
        elif digit[i] == 'W':
            withdraw.append(digit[i+1])

total_deposit = 0
total_withdraw = 0
for d in deposit:
    total_deposit += int(d)
for w in withdraw:
    total_withdraw += int(w)

total = total_deposit - total_withdraw

print(total)




