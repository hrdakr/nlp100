#I solved the chapter3 of nlp100 in https://nlp100.github.io/ja/ch03.html 

import re

with open('A20.txt', 'r', encoding='utf-8') as f:
    for row in f:
        line = row.strip()
        word =  re.search(r"\[Category:(\w+)", line)
        if word:
            print(word.group(1))
