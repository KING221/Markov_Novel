#!/usr/bin/python
# -*- coding: UTF-8 -*-
import jieba.posseg as psg
import nltk
from collections import Counter
import nltk.corpus
import random
path1 = r'D:\【图书馆】\HP4-TEST.txt'
path2 = r'D:\【图书馆】\HP4-OUT.txt'

#对文本分词，得到缓存文件
def cut_cache():
    file = open(path1, "r", encoding='utf-8').read()
    story_with_attr = [(x.word, x.flag) for x in psg.cut(file) if len(x.word)>=2] #这里是一个列表推导式
    with open(path2, "w+", encoding='utf-8') as f:
        print("writing to txt...")
        for x in story_with_attr:
            f.write("{0}\n".format(x[0]))

#读取缓存文件，得到【单词】列表
def read_result():
    pairs = []
    wordict = {}
    with open(path2, "r", encoding='utf-8')as f:
        for x in f.readlines():
            pair = x.split()
            if len(pair) < 2:
                continue
            else:
                pairs.append((pair[0]))
                words = [pairs]
                for i in range(1, len(pairs)):
                    if words[i-1] not in wordict:
                      wordict[words[i-1]] = {}
                    if words[i] not in wordict[words[i-1]]:
                        wordict[words[i-1]][words[i]] = 0
                    wordict[words[i-1]][words[i]] += 1
                return wordict

def get_topn(words,topn):
    c = Counter(words).most_common(topn)
    dict = {}
    with open(path2, "w+", encoding='utf-8') as f :
        for x in c:
            f.write('{0}\t{1}\n'.format(x[0], x[1]))
            dict[x[0]] = x[1]

def randword(cfd, word='哈利', num=200):


def main():
    cut_cache()
    pairs = read_result()
    chain = ''
    for i in range(num):
        chain += word
        word = randword(worddict[word])
    randword(worddict)

if __name__ == '__main__':
    main()
