#I solved the chapter3 of nlp100 in https://nlp100.github.io/ja/ch03.html 
#ref https://amaru-ai.com/entry/2022/10/06/084919

import json 

with open('A20.txt', 'w', encoding='utf-8') as g:
    with open('jawiki-country.json', 'r', encoding="utf-8") as f:
        for row in f:
            line = json.loads(row)
            if line['title'] == 'イギリス':
                text_uk = line['text']
    g.write(text_uk)

#ref2 https://kakedashi-engineer.appspot.com/2020/05/09/nlp100-ch3/
#by using panda

# import pandas as pd
# wiki = pd.read_json('jawiki-country.json', lines = True)
# uk = wiki[wiki['title']=='イギリス'].text.values
# print (uk)