#I solved the chapter1 of nlp100 in https://nlp100.github.io/ja/ch01.html 

print("A.00")
print("stressed"[::-1])

print("A.01")
p = 'パタトクカシーー'[::2]
t = 'パタトクカシーー'[1::2]
print(p)
print(t)

print("A.02")
x = ''
for i in range(len(p+t)):
    if i % 2 == 0:
        x += p[i//2::len(p)]
    else:
        x += t[(i-1)//2::len(t)]
print(x)

print("A.03")
sentence03 = 'Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.'
s0 = sentence03.replace(',','')
s1 = s0.replace('.','')
words03 = s1.split()
y=[]
for i in range(len(words03)):
    y += [len(words03[i])]
print(y)

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

