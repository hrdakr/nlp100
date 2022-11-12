#I solved the chapter1 of nlp100 in https://nlp100.github.io/ja/ch02.html 

x = []
with open('col1.txt','r') as f:
    for row in f:
        x += [row.split('\n')[0]]
    
names =sorted( set(x))
print(names)