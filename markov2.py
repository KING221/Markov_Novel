#!/usr/bin/python
# -*- coding: UTF-8 -*-
from random import randint

path1 = r'D:\【图书馆】\HP4-TEST.txt'
path2 = r'D:\【图书馆】\HP4-OUT.txt'

def makeDict(text):
    #替换换行符和引号
    text = text.replace('\n', ' ')
    text = text.replace('\“', '')
    text = text.replace('\”', '')
    punc = ['，', '。', '？', '；', ':', '!']#标记所有标点符号
    for symbol in punc:
        text = text.replace(symbol, ' '+symbol+' ')
    words = [word for word in text if word != ''] #得到每一个字
    wordict = {}
    for i in range(1, len(text)):
        if words[i-1] not in wordict:#词频计数器
            wordict[words[i-1]] = {}
        if words[i] not in wordict[words[i-1]]:
            wordict[words[i-1]][words[i]] = 0
        wordict[words[i-1]][words[i]] += 1
    return wordict#词典，带有词频

def wordLen(wordict):
    sum = 0
    for key, value in wordict.items():
       sum += value #计算该词的总体频次
    return sum

def retriveRandomWord(wordict):
    randindex = randint(1, wordLen(wordict))
    for key, value in wordict.items():
        randindex -= value
        if randindex <= 0:
            return key

def main():
    with open(path1, 'r', encoding='utf-8') as f:
        t = f.read()
    text = str(t)
    wordict = makeDict(text)

    length = 800
    chain = ''
    currentword = '哈'
    for i in range(0, length):
        chain += currentword
        currentword = retriveRandomWord(wordict[currentword])
        chain = chain.replace(' ', '')

    with open(path2, 'w', encoding='utf-8') as file:
        file.write(chain)
    print(chain)

if __name__ == '__main__':
    main()
