#I solved the chapter1 of nlp100 in https://nlp100.github.io/ja/ch01.html 


print("A.03")
sentence03 = 'Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.'
s0 = sentence03.replace(',','')
s1 = s0.replace('.','')
words03 = s1.split()
y=[]
for i in range(len(words03)):
    y += [len(words03[i])]
print(y)

