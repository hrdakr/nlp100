#ref https://www.sejuku.net/blog/78985

import json
 
json_file = open('test.json', 'r')
json_object = json.load(json_file)

#json_object is dict!

print (json_object["user1"])
print (json_object["user1"]["name"])
print (json_object["user1"]["hobby"])
print (json_object["user1"]["hobby"]["outdoor"])