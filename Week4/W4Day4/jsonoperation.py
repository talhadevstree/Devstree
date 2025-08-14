# Read, modify, and write JSON files with complex nested structures
import json


#read
with open('server.json','r') as r:
    data = json.load(r)
    print(data)

#write
data["user"]["profile3"] = {
    "name":"john",
    "email":"john001@gmail.com"
}

with open('server.json','a') as w:
    json.dump(data, w)

#modify
data["user"]["profile1"]["name"] = "john"

with open('server.json' , 'w') as m:
    json.dump(data , m)

# json.dump vs json.dumps ?