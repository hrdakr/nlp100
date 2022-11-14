#I solved the chapter1 of nlp100 in https://nlp100.github.io/ja/ch02.html 

N =int( input())

x=0
with open('popular-names.txt','r') as f:
    for _ in f:
        x += 1

with open('A15.txt', 'w') as g:
    with open('popular-names.txt','r') as f:
        for i, row in enumerate(f):
            if i < x - N:
                continue 
            g.write(row)