#I solved the chapter1 of nlp100 in https://nlp100.github.io/ja/ch01.html 


print("A.03")
sentence = 'Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.'

s = sentence.replace('.','').replace(',','')
words = s.split()
print([len(words[i]) for i in range(len(words)) ])

#y = []
#for i in range(len(words)):
#    y += [len(words[i])]
#print(y)
