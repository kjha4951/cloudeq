import json
dic={ "name":"hii",
    "status":"byeee",
    "reply":"both"
}
   
js=json.dumps(dic ,separators =(".", " = "),)
print(js)
print(type(js))
