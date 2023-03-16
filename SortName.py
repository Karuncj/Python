n=int(input(("Enter the no of names")))
print("Enter the names")
listname=[]
for i in range(n):
    name=input()
    listname.append(name)
print(listname)
listname.sort()
print("sorted list",listname)


