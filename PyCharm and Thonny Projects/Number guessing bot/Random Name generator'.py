#list the player name and their random number
#practicing class files


import random
import names
import sys

rand_list = []

n = int(input("How many Players? "))

for _ in range(n):
    rand_list.append(names.get_full_name())
print(*rand_list, sep = "\n")

    