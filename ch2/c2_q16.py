#I solved the chapter1 of nlp100 in https://nlp100.github.io/ja/ch02.html 

N = int(input())

x=0
with open('popular-names.txt','r') as f:
    for _ in f:
        x += 1

def kan(X,n):
    m = X%n
    return [X//n for _ in range(n-m)] + [X//n + 1  for _ in range(m) ]

print(kan(x,N))
print(sum(kan(x,N))==x)

#with open('A16.txt', 'w') as g:
#PLEASE EXECUTE with "> A16.txt".

with open('popular-names.txt','r') as f:
    for k in kan(x, N):
        for i in range(k):
            print(f.readline().strip())
        print('='*20)
        
