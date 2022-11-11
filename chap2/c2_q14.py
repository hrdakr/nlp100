#I solved the chapter1 of nlp100 in https://nlp100.github.io/ja/ch02.html 

N = 20
x = 0
with open('A14.txt', 'w') as g:
    with open('popular-names.txt','r') as f:
        for row in f:
            if x <= N:
                g.write(row)
                x += 1
            else :
                break

