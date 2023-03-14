f=open("file1",'w')
f.write("Hello\nI am Karun\n")
f.close()

f=open("file1",'r')
print("using for loop\n")
for line in f:
    print(line)

print("Using while loop\n")
while True:
    line=f.readline()
    if(line==" "):
        break
        print(line)
f.close()
