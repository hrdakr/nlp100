#I solved the chapter1 of nlp100 in https://nlp100.github.io/ja/ch02.html 

ind_row = {}
name_inds = {}
name_count = {}

names = []

num = 0


with open('popular-names.txt','r') as f:
    for i , row in enumerate(f):
        ind_row.update({i: row})
        num += 1
        name = row.split('\t')[0]
        if name not in names:
            names += [name]
            name_inds.update({name : [i] })
            name_count.update({name : int(1) })
        else :
            l = name_inds.get(name) + [i]
            name_inds.update({name : l})
            
            n = name_count.get(name) + 1
            name_count.update({ name :  n})

s_name_count = sorted(name_count.items(), key = lambda item: item[1], reverse=True)
#ref.https://codechacha.com/ja/python-sorting-dict/

for name , _ in s_name_count:
    for i in name_inds.get(name):
        print(ind_row.get(i).strip())




