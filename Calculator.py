class Ist:
  a=0
  b=0
  def set_value(self,x,y):
      self.a=x
      self.b=y
  def sum(self):
      return (self.a+self.b)
  def sub(self):
      return (self.a-self.b)
  def mul(self):
      return (self.a*self.b)
  def div(self):
      return (self.a/self.b)


class IInd:
  a=0
  b=0
  def set_value(self,x,y):
      self.a=x
      self.b=y
  def sum(self):
      return (self.a+self.b)
  def sub(self):
      return (self.a-self.b)
  def mul(self):
      return (self.a*self.b)
  def div(self):
      return (self.a/self.b)

x=int(input("First Number : "))
z=str(input("Process : "))
y=int(input("Second Number : "))
fst=Ist()
fst.set_value(x, y)
if(z=='+'):
   p=fst.sum() 
   print(fst.sum())
elif(z=='-'):
    p=fst.sub()
    print(fst.sub())
elif(z=='*'):
   p=fst.mul()
   print(fst.mul())
elif(s=='/'):
    print(mst.div())
    p=mst.div()
else :
    print("OOPs wrong entry")

print("Do you want to further Move")
x=int(input("if Yes then press-1 if No then press-0 : "))
if(x==1):
    while(1):
        s=str(input("Enter Process : "))
        t=int(input("Enter Second Number : "))
        mst=IInd()
        mst.set_value(p,t)
        if(s=='+'):
           print(mst.sum())
           p=mst.sum()
        elif(s=='-'):
            print(mst.sub())
            p=mst.sub()
        elif(s=='*'):
            print(mst.mul())
            p=mst.mul()
        elif(s=='/'):
            print(mst.div())
            p=mst.div()
        else :
            print("OOPs wrong entry")
        print("Do want to continue")
        x=int(input("if Yes then press-1 if No then press-0 : "))
        if(x==0):
          break
        else:
           print(".........Thank You.........")
else:
    print(".........Thank You.........")
