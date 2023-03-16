n=int(input(("Enter the no of elements")))
print("Enter the elements")
list1=[]
for i in range(n):
    name=input()
    list1.append(name)
print("Entered list=",list1)
uniq=[]
for i in list1:
    if i not in uniq:
        uniq.append(i)
print("Unique list=",uniq)

