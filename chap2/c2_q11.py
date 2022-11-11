#I solved the chapter1 of nlp100 in https://nlp100.github.io/ja/ch02.html 

# with open('popular-names_notab.txt', 'w') as g:
#     with open('popular-names.txt','r') as f:
#         s = f.readlines()
#         for n in range(len(s)):
#             g.write(s[n].replace('\t',' ') )

with open('popular-names_notab.txt', 'w') as g:
    with open('popular-names.txt','r') as f:
        for row in f:
            g.write( row.replace('\t',' '))