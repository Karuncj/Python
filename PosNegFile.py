n=int(input("Enter the no of elements"))
f=open("file.txt","w")
print("Enter the elements")
for i in range(n):
    ele=(input())
    f.write(ele+"\n")
f.close()
f=open("file.txt","r")
p=open("Pos.txt","w")
n=open("Neg.txt","w")
for line in f:
    if(int(line)>=0):
        p.write(str(line))
    else:
        n.write(str(line))
p.close()
n.close()
p=open("Pos.txt","r")
n=open("Neg.txt","r")

print("Positive list=\n",p.read())
print("Negetaive list=\n",n.read())
