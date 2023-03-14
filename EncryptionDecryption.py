distance=int(input("Enter the distance:"))
word=input("Enter sentence:")
code=""
sentence=""
#encryption
for i in word:
    if(i==" "):
        code=code+" "
        continue
    asc=ord(i)
    if(asc<=90):
        ceaser=asc+distance
        if(ceaser>ord('Z')):
            ceaser=(ceaser-65)%26+65        
    else:
        ceaser=asc+distance
        if(ceaser>ord('z')):
            ceaser=(ceaser-97)%26+97
    code=code+chr(ceaser)
#decryption
for i in code:
    if(i==" "):
        decode=decode+" "
        continue
    asc=ord(i)
    if(asc<=90):
        ceaser=asc-distance
        if(ceaser>ord('Z')):
            ceaser=(ceaser-65)%26+65        
    else:
        ceaser=asc-distance
        if(ceaser>ord('z')):
            ceaser=(ceaser-97)%26+97
    code=code+chr(ceaser)
print("ceaser decoded of ",word,"is ",code)
