#I solved the chapter1 of nlp100 in https://nlp100.github.io/ja/ch01.html 

print("A.02")
x = ''
for i in range(len(p+t)):
    if i % 2 == 0:
        x += p[i//2::len(p)]
    else:
        x += t[(i-1)//2::len(t)]
print(x)

