#I solved the chapter3 of nlp100 in https://nlp100.github.io/ja/ch03.html 

import re
import json

with open('A20.txt', 'r', encoding='utf-8') as f:
    for row in f:
        line = row.strip()
        word =  re.findall(r'(\=+)(\w+)(\=+)', line)
        if word:
            output =  ''.join(str(word[0][1]) + ':' + str( len(word[0][0]) -1 ))
            print(output)
            

# with open('jawiki-country.json', 'r', encoding="utf-8") as f:
#     for row in f:
#         line = json.loads(row)
#         if line['title'] == 'イギリス':
#             text_uk = line['text']
# pattern = r'(\=+)(\w+)(\=+)'
# print(re.findall(pattern, text_uk, re.MULTILINE))
#result = '\n'.join(i[1] + ':' + str(len(i[0]) - 1) for i in re.findall(pattern, text_uk, re.MULTILINE))
#print(result)