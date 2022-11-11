#I solved the chapter1 of nlp100 in https://nlp100.github.io/ja/ch02.html 

with open('popular-names.txt','r') as f:
    with open('col1.txt', 'w') as g1:
        with open('col2.txt', 'w') as g2:
                for row in f:
                    g1.write( row.split('\t')[0] +'\n' )
                    g2.write( row.split('\t')[1] +'\n' )
        
