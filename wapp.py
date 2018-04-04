#! /usr/bin/python3

from collections import defaultdict
import operator

FILENAME = 'delanje.txt'

lines = []

with open(FILENAME) as f:
    lines = f.readlines()

freq = defaultdict(int) 

last_name = ""

for line in lines:
    if not line[0] == '[': 
        continue
    line = line[len('[20.02.2017. 13:47:16] '):]
    index = line.find(':')

    if index == -1:
        continue

    name = str(line[:index])
    if freq[name] == 0:
        print ("novo ime: " + name)

    if name != last_name:   
        freq[name] = freq[name] + 1

    last_name = name


sorted_x = sorted(freq.items(), key=operator.itemgetter(1), reverse=True)

print ("alo ispis: +++++++++++++++++++++++")

for e in sorted_x:
    print (e[0] + ": " + str(e[1]))
    
