#ref https://www.sejuku.net/blog/78985

import re

src = "私は4月1日は焼き肉を食べて、4月2日はうを食べて、4月13日はタラコを食べた。"
re.findall(r"\d月\d{1,2}日", src) #\dは数字を表す特殊文字
print(re.findall(r"\d月\d{1,2}日", src))

# ['4月1日', '4月2日', '4月13日']

re.findall(r"(\d月\d{1,2}日)は(\w+?)を食べ", src)
print(re.findall("(\d月\d{1,2}日)は(\w)を食べ", src))
# [('4月1日', '焼き肉'), ('4月2日', '寿司'), ('4月13日', 'タラコ')]

seq = "[[Category:英連邦王国|*]]"

print(re.findall(r"Category:(\w+)", seq)[0])