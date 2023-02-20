'''
You are required to write a program to sort the (name, age, height) tuples by ascending order where name is
string, age and height are numbers. The tuples are input by the console. The sort criteria is:
1: Sort based on name;
2: Then sort based on age;
3: Then sort by score.
The priority is that name > age > score.
If the following tuples are given as input to the program:
Tom,19,80
John,20,90
Jony,17,91
Jony,17,93
Json,21,85
Then, the output of the program should be:
[('John', '20', '90'), ('Jony', '17', '91'), ('Jony', '17', '93'), ('Json', '21', '85'), ('Tom', '19', '80')]
'''

multiline = []
all_data = []

while True:
    line = input('Enter your data = ')
    if line:
        multiline.append(line)
        # data = line.split('\n')
        # a = str(data).split()
        # total_data.append(a)
    else:
        break
    data = line.split(',')
    all_data.append(data)

all_name = []
all_age = []
all_score = []
total_data = []
print(all_data)

for i in all_data:
    all_name.append(all_data[i][0])
    all_age.append(all_data[i][1])


print(total_data)
print(all_name)
print(all_age)
print(all_score)


# for i in range(len(all_data)):
    # all_name.append(all_data[i][0])
    # all_age.append(all_data[i][1])
    # all_score.append(all_data[i][2])
    # my = all_data[i]
    # print(my)

# print(all_name, all_age, all_score)