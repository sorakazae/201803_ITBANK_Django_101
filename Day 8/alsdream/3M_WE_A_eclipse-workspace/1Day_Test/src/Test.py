class Person():
    def __init__(self,name,age,contry):
        self.name = name
        self.age = age
        self.contry = contry
    
    def work(self):
        print("man is work")
        
    def eat(self,something):
        print('%s eat %s'%(self.name,something))
        
class Korean(Person):
    def __init__(self,name,age):
        super(Korean,self).__init__(name,age,"korea")
        
    def eat(self,something):
        if something == "kimchi":
            print("do you know kimchi?")
        else:
            super(Korean,self).eat(something)
        
obj1 = Person('shin',30,'usa')
obj1.work()
obj1.eat('kimchi')
obj1.eat('cake')

        
        
