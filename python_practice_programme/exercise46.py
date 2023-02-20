'''
Write a program which can filter even numbers in a list by using the filter function. The list is:
[1,2,3,4,5,6,7,8,9,10].
Use filter() to filter some elements in a list.
Use lambda to define anonymous functions.
'''

list1 = [1,2,3,4,5,6,7,8,9,10]


def FindEven(x):
    if x % 2 == 0:
        return True
    else:
        return False


def Myfunction():
    mynum = filter(FindEven, list1)
    mylist = []
    for i in mynum:
        mylist.append(i)
    print(mylist)
Myfunction()