f=open("file","w")
print("Enter 10 numnbers to write to file")
for i in range(0,10):
    n=input()
    f.write(n+"\n")
f.close()
f=open("file","r")
sum=0
for line in f:
    num=int(line)
    sum=sum+num
print("sum=",sum)
f.close()


'''Another Method

f=open("file","w")
print("Enter 10 numnbers to write to file")
for i in range(0,10):
    n=input()
    f.write(n+" ")
f.close()
f=open("file","r")
sum=0
for line in f:
        l=line.split()
        for j in l:
            num=int(j)
            sum=sum+num
print("sum=",sum)
f.close()

'''
