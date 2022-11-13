#ref https://www.sejuku.net/blog/78985

import json
 
json_file = open('test.json', 'r')
json_object = json.load(json_file)
 
 
print(type(json_object))
print(json_object)
print(json_object["user1"])
 
json_string = json.dumps(json_object)
 
print("****************************")
print(type(json_string))
print(json_string)
# print(json_string["user1"])
# ただの文字列なのでエラーになる