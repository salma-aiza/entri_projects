class employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def empl_desc(self):
        self.name=input("enter your name")
        self.salary=int(input("enter your salary"))
    def display(self):
        print(self.name,self.salary)
class hr:
    def hr_function(self):
        print("hi am child class...am hr")
class manager(hr,employee):
    def manager_fun(self):
        print("am child class..am manager")

obj=manager('','')
obj.empl_desc()
obj.display()
obj.hr_function()
obj.manager_fun()
