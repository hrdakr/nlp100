#I solved the chapter1 of nlp100 in https://nlp100.github.io/ja/ch01.html 

print("A.06")

s = "paraparaparadise"
t = "paragraph"

def letter_n_gram(n, sentence):
    x = []
    for i in range(len(sentence)):
        if i + n <= len(sentence):
            x.append(sentence[i:i+n])
        else:
            break
    return x

X = letter_n_gram(2, s )
Y = letter_n_gram(2, t )

def setminus(list1, list2):
    return [i for i in list1 if i not in list2 ]

print(X or Y)
print(X and Y)
print(setminus(X, Y))

def search(word, str):
    list = letter_n_gram(2, str)
    if word in list :
        print('%s is in %s !' % (word , str))
    else :
        print('%s is NOT in %s !' % (word , str))

search( 'se' , s)
search('se', t)
