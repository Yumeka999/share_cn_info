# encoding:utf-8

import os
import json
import pandas as pd

df = pd.read_excel("汉语拼音+注音符号+威妥玛拼音+国语罗马字+注音符号第二式+耶鲁拼音+通用拼音 对照表.xlsx")
ls_col = df.columns.values.tolist()

m_py_dct = {e:{} for e in ls_col[1:]}
print(m_py_dct)

for i in range(df.shape[0]):
    s_py = df.iloc[i,0]
    for j in range(1, df.shape[1]):
        s_py_map = df.iloc[i,0]
        s_type = ls_col[j]

        m_py_dct[s_type][s_py] = {"val":s_py_map, "type":s_type}

# m_out = df.to_dict('index')
# # print(m_out)

with open("all_pinyin_map.json", "w", encoding='utf-8') as fp:
    fp.write(json.dumps(m_py_dct, ensure_ascii=False))
