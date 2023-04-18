class Arith:
    def read(self):
        self.n1=int(input("enter first number:"))
        self.n2=int(input("Enter second number:"))
    
    def sum(self):
        sum=self.n1+self.n2
        print("sum=",sum)
        
a=Arith()
a.read()
a.sum()

