#I solved the chapter1 of nlp100 in https://nlp100.github.io/ja/ch02.html 
"""
with open('popular-names.txt','r') as f:
    #for row in f:
    #    print (row.strip())
    print(len(f.readlines()))
"""

x=0
with open('popular-names.txt','r') as f:
    for _ in f:
        x += 1
print(x)