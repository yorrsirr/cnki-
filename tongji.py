# -*- coding:utf-8 -*-
import sys

reload(sys)
sys.setdefaultencoding("utf-8")
import os
import jieba
import jieba.analyse

##########利用jieba对收集好的摘要文件zhaiyao.txt进行分词，得到分词后的摘要文件seg.txt##########
with open('seg.txt','w') as w:#打开文件‘seg.txt’命名为w
    with open('zhaiyao', 'r') as f1:#打开文件‘zhaiyao’命名为f1
        word = f1.readline() #逐行读取
        while word:
            tags = jieba.cut(word) #用jieba对句子进行分词
            tagsw = " ".join(tags) #空格连接切分的词
            w.write(tagsw) #将tagsw写入文件w
            word = f1.readline() #逐行读取
    f1.close() #关闭文件f1
w.close() #关闭文件w

##########对分词后的摘要文件seg.txt进行词频统计，得到词频统计结果word.txt##########
word_lst = [] #用来存所有词的列表
word_dict = {} #用来存所有词及其频次的字典
wf1 = open('seg.txt')
wf2 = open("word.txt", 'w')

for line in wf1: #line为wf1中的每一行
    lines = line.split() #将句子line以空格或换行符进行分割，返回列表lines，每一个元素代表每一个词
    for each in lines:
        word_lst.append(each) #往列表word_lst加入each

for item in word_lst: #item为列表word_list中的每个词
    if item not in word_dict: #如果词item不在字典word_dict中，则初始化该词的频次为1
        word_dict[item] = 1
    else:
        word_dict[item] += 1 #若词item已在字典word_dict中，则该词的频次加1

for key in word_dict: #对于字典word_dict里面的每个键
    print key, word_dict[key] #打印键+键值
    wf2.write(key + ' ' + str(word_dict[key]) + '\n') #写入文档

