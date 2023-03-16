n=int(input("Enter the no of elements"))
list1=[]
print("Enter the elements")
for i in range(n):
    ele=int(input())
    list1.append(ele);
PosList=[]
NegList=[]
for i in list1:
    if(i>=0):
        PosList.append(i)
    else:
        NegList.append(i)
print("Positive list=",PosList)
print("Negetaive list=",NegList)
