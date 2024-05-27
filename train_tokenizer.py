from tokenizer import BPETokenizer
from config import *
import os
import sys 
import json 

if os.path.exists('tokenizer.bin'):
    print('tokenizer.bin已存在')
    sys.exit(0)

# 原始数据
with open('纳兰性德诗集.json','r',encoding='utf-8') as fp:
    ds=json.loads(fp.read())
for line in open("poetry_data.json", "r", encoding="utf-8").readlines():
    obj = json.loads(line.strip())
    ds.append(obj)

text_list=[]
sample_count=0
for sample in ds:
    text_list.append(sample['title'])
    for p in sample['para']: 
        text_list.append(p)
    sample_count+=1
print('共加载%d条数据'%sample_count)

# 训练词表
tokenizer=BPETokenizer()  
tokenizer.train(text_list,VOCAB_SIZE)
tokenizer.add_special_tokens([IM_START,IM_END,BOS,EOS,PAD])
tokenizer.save('tokenizer.bin')