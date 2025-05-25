class num:
    first=0
    sec=0
    ans=0
    
    def __init__(self,f,s):
        self.first=f
        self.sec=s
        
    def add(self):
        self.answer = self.first + self.sec
        print("Answer :", self.answer,' = ',self.first," + ",self.sec )
        
    def sub(self):
        self.answer = self.first - self.sec
        print("Answer :", self.answer,' = ',self.first," - ",self.sec )
    
    def product(self):
        self.answer = self.first * self.sec
        print("Answer :", self.answer,' = ',self.first," * ",self.sec )
        
    def division(self):
        self.answer = self.first / self.sec
        print("Answer :", self.answer,' = ',self.first," / ",self.sec )
op=input("which operation would you do \n1.+\n2.-\n3.*\n4./\n:")
first=int(input("first num :"))
sec=int(input("second num :"))

c=num(first,sec)



if op=="1":
    c.add()

if op=="2":
    c.sub()
    
if op=="3":
    c.product()
    
if op=="4":
    c.division()
    
