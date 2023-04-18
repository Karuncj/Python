class vechicle:
    def __init__(self,model,year,price):
        self.model=model
        self.year=year
        self.price=price
    def cost(self):
        print("The price=",self.price)
v=vechicle("ford",2023,"80L")
v1=vechicle("ford",2022,"50L")
v.cost()
v1.cost()
