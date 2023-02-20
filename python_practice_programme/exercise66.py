'''
Write a program to read an ASCII string and to convert it to a unicode string encoded by utf-8.
Use the unicode() function to convert.
'''

ustring = u'Hello world \u018e \xf1'

converted = ustring.encode('utf-8')

print(converted)