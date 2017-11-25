import sys
import random
import os

n = int(input())
for i in range(n):
    string = str(input())
    print(string[::2],string[1::2])