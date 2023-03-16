n=int(input("Enter the no of elements:"))
list1=[]
for i in range(n):
    list1.append(input())
el=input("Enter the elment to be found:")
if el in list1:
    print(list1.index(el))
else:
    print("Not found")
