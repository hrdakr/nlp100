#I solved the chapter1 of nlp100 in https://nlp100.github.io/ja/ch02.html 

N =int( input())

with open('A14.txt', 'w') as g:
    with open('popular-names.txt','r') as f:
        for i, row in enumerate(f):
            if i <= N:
                g.write(row)
            else :
                break

