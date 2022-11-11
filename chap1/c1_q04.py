#I solved the chapter1 of nlp100 in https://nlp100.github.io/ja/ch01.html 

print("A.04")
sentence04 = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
s2 = sentence04.replace('.','')
words04 = s2.split()

m = [1, 5, 6, 7, 8, 9, 15, 16, 19]
z = []
for i in range(len(words04)):
    if i+1 in m:
        z += (words04[i])[0]
    else :
        z +=[''.join( (words04[i])[0] + (words04[i])[1] )]

data={}
for i in range(len(words04)):
    data.update({z[i]:i+1})
print(data)
