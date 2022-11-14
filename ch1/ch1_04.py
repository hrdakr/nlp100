#I solved the chapter1 of nlp100 in https://nlp100.github.io/ja/ch01.html 

print("A.04")
sentence = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
s = sentence.replace('.','')
words = s.split()
m = [1, 5, 6, 7, 8, 9, 15, 16, 19]

data = {}
for i , word in enumerate(words):
    if i+1 in m :
        data[(words[i])[0]] = i+1
    else :
        data[(words[i][:2])] = i+1

print(data)

'''
z = []
for i in range(len(words)):
    if i+1 in m:
        z += (words[i])[0]
    else :
        z +=[''.join( (words[i])[0] + (words[i])[1] )]

data={}
for i in range(len(words)):
    data.update({z[i]:i+1})
print(data)
'''