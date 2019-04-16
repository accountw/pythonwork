# -*- coding: utf-8 -*-
"""
Created on 2019年3月31日
统计一篇英文文章各个单词出现的词频，并按单次的词频从大到小用词云输出。
@author:
软工4班
张宝
201610414427

"""

import re
import collections
from wordcloud import WordCloud




def count_word(path):
    result = {}
    with open(path) as file_obj:
        all_the_text = file_obj.read()
        
        #大写转小写
        all_the_text = all_the_text.lower()
        #正则表达式替换特殊字符
        all_the_text = re.sub(r'[,.;?"]', "", all_the_text)
        wordcloud=WordCloud().generate(all_the_text)
        image_produce=wordcloud.to_image()
        image_produce.show()
        for word in all_the_text.split():
            if word not in result:
                result[word] = 0
            result[word] += 1 
        return result

def sort_by_count(d):
    d = collections.OrderedDict(sorted(d.items(), key = lambda t: -t[1]))
    return d

if __name__ == '__main__':
    file_name = "D:\pythonwork\english.txt"
    dword = count_word(file_name)
    dword = sort_by_count(dword)
    for key,value in dword.items():
        print(key+ ":%d" %(value))
        
        
        