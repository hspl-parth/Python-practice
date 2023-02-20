'''
Please write a program to compress and decompress the string "hello world!hello world!hello world!hello
world!".
Use zlib.compress() and zlib.decompress() to compress and decompress a string.
'''

import zlib

str1 = b'hello world!hello world!hello world!hello world!'

compressstr1 = zlib.compress(str1)

decompressstr1 = zlib.decompress(compressstr1)

print(len(str1))
print(len(compressstr1))
print(len(decompressstr1))
