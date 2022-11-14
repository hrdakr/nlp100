#I solved the chapter1 of nlp100 in https://nlp100.github.io/ja/ch01.html 

import random

print("A.09")

sentence = "I couldn’t believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
words = sentence.split()

x = []
for word in words:
    n = len(word)
    if n <= 4 :
        x +=[ word]
    else :
        y =  word[0]  + ''.join(random.sample( word[ 1 : n - 1 ],  n-2 )) + word[n-1] 
        x += [y]
print(' '.join(x))
