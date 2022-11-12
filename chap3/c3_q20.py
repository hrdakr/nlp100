#I solved the chapter3 of nlp100 in https://nlp100.github.io/ja/ch03.html 
#ref https://amaru-ai.com/entry/2022/10/06/084919
import json 

#with open('A20j.json', 'r', encoding="utf-8") as g:
with open('jawiki-country.json', 'r', encoding="utf-8_sig") as f:
    for row in f:
        line = json.loads(row)
        if line['title'] == 'イギリス':
            text_uk = line['text']
        else:
            continue
print(text_uk)
