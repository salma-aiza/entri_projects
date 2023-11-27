
class employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def empl_desc(self):
        self.name=input("enter your name")
        self.salary=int(input("enter your salary"))
    def display(self):
        print(self.name,self.salary)
class hr(employee):
    def hr_function(self):
        print("hi am child class...am hr")
class manager(hr):
    def manager_fun(self):
        print("am child class..am manager")
class ceo(manager):
    def ceo_fun(self):
        print("am child class3...am ceo")

ceo1=ceo('','')
ceo1.empl_desc()
ceo1.display()
ceo1.hr_function()
ceo1.manager_fun()
ceo1.ceo_fun()