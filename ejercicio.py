i = 4
d = 4.0
s = 'HackerRank '

inter = input("Ingrese un número: ")
double = input("Ingrese un double: ")
string = input("Ingrese un string: ")

print (i + int(inter))
print (d + float(double))
print (s + string)



import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input("De qué número querés la tabla? "))

    for i in range(1, 101):
        print("{} x {} = {}".format(n, i, (n*i)))


t= int(input())

for i in range(0,t):
    S = input()
    print(S[0::2] +" "+S[1::2])