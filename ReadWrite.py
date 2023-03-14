f=open("file1",'w')
s=input("Enter a string ro write to the file:")
f.write(s)
f.close()

f=open("file1",'r')
print(f.read())
f.close()
