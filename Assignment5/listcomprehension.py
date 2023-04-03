name=["komal","moizamam","renu","puja","pallavi"]
name1=[x.upper() for x in name]
name2=[x for x in name if "i" in x]
name3=["hello" for x in name]
name4=[x if x!= "komal" else "moizamam" for x in name]

print(name1)
print(name2)
print(name3)
print(name4)
