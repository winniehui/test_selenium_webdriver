import json

json_data = {
    "results":[
        {
            "location":{
                "id":"WX32440JJ443",
                "name":"北京",
                "country":"cn",
                "path":"北京，北京",
                "timezone":"Asia/shanghai",
                "timezone_offset":"+08:00"
            }
        }
    ]
}

f = open('test.txt','w')
print(type(f))
json.dump(json_data,f)
f.close()

b = json.dumps(json_data)
print(b,type(b),"\n")
c = json.loads(b)
print(c,type(c))