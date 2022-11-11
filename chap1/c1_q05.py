#I solved the chapter1 of nlp100 in https://nlp100.github.io/ja/ch01.html 

print("A.05")

def letter_n_gram(n, sentence):
    x = []
    for i in range(len(sentence)):
        if i + n <= len(sentence):
            x.append(sentence[i:i+n])
        else:
            break
    return x
    

def word_n_gram(n, sentence):
    words = sentence.split()
    x = []
    for word in words:
        if len(word) <n :
            x.append(word)
        else :
            for i in range(len(word)):
                if i+n-1 in range(len(word)):
                    x.append(word[i:n+i])
                else:  
                    break
    return x


print(letter_n_gram(2, "I am an NLPer"))
print(word_n_gram(2, "I am an NLPer"))

