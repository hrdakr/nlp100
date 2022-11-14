#I solved the chapter3 of nlp100 in https://nlp100.github.io/ja/ch03.html 

import re
import json

output =''
with open('A24.txt', 'w', encoding='utf-8') as g:
    with open('A20.txt', 'r', encoding='utf-8') as f:
        for row in f:
            line = row.strip()
            word =  re.findall(r'\[\[ファイル:(.+?)\|', line)
            if word:
                output += word[0] + '\n'
    g.write(output.strip())


# with open('jawiki-country.json', 'r', encoding="utf-8") as f:
#     for row in f:
#         line = json.loads(row)
#         if line['title'] == 'イギリス':
#             text_uk = line['text']

# print(text_uk[0:10])
