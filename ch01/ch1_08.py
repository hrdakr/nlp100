#I solved the chapter1 of nlp100 in https://nlp100.github.io/ja/ch01.html 

print("A.08")
s = input("文字列を入力")

def cipher(sentence):
    x = ''
    for letter in sentence:
        n = ord(letter)
        if 97 <= n <= 122:
            m = 219 - n
            x += chr(m)
        else:
            x += letter
    return x
    
print( cipher(s) )