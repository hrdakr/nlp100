#I solved the chapter1 of nlp100 in https://nlp100.github.io/ja/ch02.html 

col1 = []
with open('col1.txt','r') as f:
    for row in f:
        col1 += [row.split('\n')[0]]
    
names =sorted( set(col1))
print(names)