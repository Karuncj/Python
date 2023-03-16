list1=[]
n=int(input("Enter the no of elements"))
print("Enter the elements:")
for i in range(n):
    ele=int(input())
    list1.append(ele)
list1.sort()
print(list1)
if(n%2==0):
    term1=list1[int((n/2))]
    term2=list1[int((n/2))+1]
    print(term1,term2)
    med=int((term1)+(term2)/2)-1
else:
    med=int((n+1)/2)-1
    print(med)
print("median=",list1[med])
