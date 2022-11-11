#I solved the chapter1 of nlp100 in https://nlp100.github.io/ja/ch01.html 

print("A.08")
s = input("文字列を入力")

def letter_n_gram(n, sentence):
    x = []
    for i in range(len(sentence)):
        if i + n <= len(sentence):
            x.append(sentence[i:i+n])
        else:
            break
    return x

def cipher(sentence):
    letters = letter_n_gram(1, sentence)
    x = ''
    for letter in letters:
        n = ord(letter)
        if n in range(97, 123):
            m = 219 - n
            x += chr(m)
        else:
            x += letter
    return x
    
print( cipher(s) )