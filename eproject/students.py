class students:
    def details(self,name,m1,m2,m3):
        self.name=name
        self.m1=m1
        self.m2=m2
        self.m3=m3
    def display(self):
        self.name=input("enter your name:")
        self.m1=int(input("enter your first mark:"))
        self.m2=int(input("enter your second mark:"))
        self.m3=int(input("enter your third mark:"))
    def total_mark(self,total):
        self.total=total
        self.total=self.m1+self.m2+self.m3

        print("total=",self.m1+self.m2+self.m3)
    def average_mark(self,avg):
        self.avg=avg
        self.avg = self.total / 3
        print("average mark is",self.total/3)
    def check(self):
        if self.avg>=80:
            print("student passed")
        else:
            print("student failed")

student=students()
student.details('','','','')
student.display()
student.total_mark('')
student.average_mark('')
student.check()