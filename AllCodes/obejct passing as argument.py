class a:
    classAnumber=0
    def classAmethod(self,num):
        self.classAnumber = num
class b:
    classBnumber=0
    def classBmethod(self,obj):
        self.classBnumber = obj.classAnumber
        print(self.classBnumber)
        
x = a()
x.classAmethod(10)

y = b()
y.classBmethod(x)