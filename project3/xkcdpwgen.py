#!/usr/bin/env python3

import sys

import random

import argparse

WORDS, CAPS, NUMBERS, SYMBOLS = 4, 0, 0, 0

symbolsList = ['~', '!', '@', '#', '$', '%', '^', '&', '*', '.', ':', ':']

argsNum = len(sys.argv)

parser = argparse.ArgumentParser()
parser.add_argument('-w', '--words', help='include WORDS words in the password '
                                          '(default=4)')
parser.add_argument('-c', '--caps', help='capitalize the first letter of CAPS random words '
                                         '(default=0)')
parser.add_argument('-n', '--numbers', help='insert NUMBERS random numbers in the password '
                                            '(default=0)')
parser.add_argument('-s', '--symbols', help='insert SYMBOLS random symbols in the password '
                                            '(default=0)')
parser.parse_args()

for x in range(1, argsNum - 1):
    curr = sys.argv[x]
    if (curr == "-w") or (curr == "--words"):
        WORDS = int(sys.argv[x+1])
        x = x+1
    if (curr == "-c") or (curr == "--caps"):
        CAPS = int(sys.argv[x+1])
        x = x+1
    if (curr == "-n") or (curr == "--numbers"):
        NUMBERS = int(sys.argv[x+1])
        x = x+1
    if (curr == "-s") or (curr == "--symbols"):
        SYMBOLS = int(sys.argv[x+1])
        x = x+1
if CAPS > WORDS:
    print("invalid arg: CAPS > WORDS  -  setting CAPS = WORDS")
    CAPS = WORDS

wordsList = []

for y in range(0, WORDS):
    currWord = random.choice(list(open('corncob_lowercase.txt'))).rstrip("\r\n")
    if CAPS == 0:
        wordsList.append(currWord)
    else:
        wordsList.append(currWord.capitalize())
        CAPS = CAPS - 1

for z in range(0, NUMBERS):
    currLen = len(wordsList)
    currInd = random.randint(0, currLen)
    randInt = str(random.randint(0, 9))

    if currInd == currLen:
        wordsList.append(randInt)
    else:
        wordsList.insert(currInd, randInt)


for i in range(0, SYMBOLS):
    currLen = len(wordsList)
    currInd = random.randint(0, currLen)
    randSymbol = str(random.choice(symbolsList))

    if currInd == currLen:
        wordsList.append(randSymbol)
    else:
        wordsList.insert(currInd, randSymbol)

finalString = ""

while len(wordsList) > 0:
    currRand = random.choice(wordsList)
    finalString = finalString + currRand
    wordsList.remove(currRand)

print(finalString)
