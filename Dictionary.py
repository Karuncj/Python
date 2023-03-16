d={"name":"Karun","age":20}
print(d)
d["place"]="kottayam"
print(d)
print(d.pop("name"))
print(d)
d[90]="a"
d[80]="b"
for i in d:
    print(i,d[i])
print(list(d.items()))
