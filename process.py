import json
import csv
import os

with open("input.txt", "r", encoding="utf-8") as fp:
    ls_all_pinyin = []
    for s_line in fp:
        s_line = s_line.strip()
        if s_line == "":
            continue
        
        ls_info = s_line.split("\t")
        
        ls_all_pinyin.append(ls_info)
        print("|" + "|".join(ls_info) + "|")
    

with open("拼音.csv", "w", encoding="utf-8") as fp:
    for ls_info in ls_all_pinyin:
        s_row = ','.join(ls_info)
        fp.write("%s\n" % s_row)

