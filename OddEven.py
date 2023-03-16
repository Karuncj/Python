n=int(input("Enter the no of elements"))
list1=[]
print("Enter the elements")
for i in range(n):
    ele=int(input())
    list1.append(ele);
oddList=[]
evenList=[]
for i in list1:
    if(i%2==0):
        oddList.append(i)
    else:
        evenList.append(i)
print("Odd list=",oddList)
print("Even list=",evenList)
