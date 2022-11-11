#I solved the chapter1 of nlp100 in https://nlp100.github.io/ja/ch02.html 
with open('col12.txt', 'w') as g:
    with open('col1.txt', 'r') as f1:
        with open('col2.txt', 'r') as f2:
            for row1, row2 in zip(f1, f2):
                g.write( row1.replace('\n','\t') + row2 )
