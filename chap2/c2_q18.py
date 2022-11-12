#I solved the chapter1 of nlp100 in https://nlp100.github.io/ja/ch02.html 

mat = {}
data = {}
col3 = []
count =0

with open('popular-names.txt','r') as f:
    for i , row in enumerate(f):
        mat.update({  i :row.strip() })
        data.update( { int(row.split('\t')[2].strip()) : i } )
        col3 += [int(row.split('\t')[2].strip())]
        count += 1

scol3 = sorted(col3, reverse=True)

for k in range(count): 
    print(mat.get( data.get(scol3[k]) ))

