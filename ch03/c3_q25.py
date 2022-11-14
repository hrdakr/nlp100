#I solved the chapter3 of nlp100 in https://nlp100.github.io/ja/ch03.html 

import json
import re

# output =''
# with open('A24.txt', 'w', encoding='utf-8') as g:
#     with open('A20.txt', 'r', encoding='utf-8') as f:
#         for row in f:
#             line = row.strip()
#             word =  re.findall(r'\[\[ファイル:(.+?)\|', line)
#             if word:
#                 output += word[0] + '\n'
#     g.write(output.strip())


##ref https://amaru-ai.com/entry/2022/10/06/084919

with open('jawiki-country.json', 'r', encoding="utf-8") as f:
    for row in f:
        line = json.loads(row)
        if line['title'] == 'イギリス':
            text_uk = line['text']

# テンプレートの抽出
pattern = r'^\{\{基礎情報.*?$(.*?)^\}\}'
template = re.findall(pattern, text_uk, re.MULTILINE + re.DOTALL)
print(template)

# フィールド名と値を辞書オブジェクトに格納
# pattern = r'^\|(.+?)\s*=\s*(.+?)(?:(?=\n\|)|(?=\n$))'
# result = dict(re.findall(pattern, template[0], re.MULTILINE + re.DOTALL))
# for k, v in result.items():
#   print(k + ': ' + v)
