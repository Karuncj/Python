list1=[]
n=int(input("Enter the no of elements"))
print("Enter the elements:")
for i in range(n):
    ele=int(input())
    list1.append(ele)
list1.sort()
max=0
for i in list1:
    if(list1.count(i)>max):
        value=i
        max=list1.count(i)
print("mode=",value)
        
