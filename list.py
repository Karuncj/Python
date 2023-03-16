#multi dimensional list
listl=[['karun',1,"chery","james",200,'karun'],2,3,5,7,5,6,3,1,]
print(listl[0][3])
print(len(listl))
print(listl[2:6])
print(listl[:6])
print(listl[-7])
listl.remove(2)
print(listl)
listl.remove(5)
print(listl)
list2="karun chery james"
print(list(list2))
list3=[]
list3.append("hello")
print(list3)
list3.append("how")
list3.insert(2,81)
list3.insert(3,"are")
#print(listl.count(3))
print(list3)
print(list3.pop(1))
print(list3)
list4=[1,5,7,2,3]
print(list4.reverse())
print(list4.sort())
list3.extend(list4)
print(list3)

