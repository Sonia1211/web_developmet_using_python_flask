class register:
    print("Welcome")
    v="Sony"
obj=register()
#print(obj)
#print(obj.v)

class register:
    def __init__(self,name,des,cl):
        self.name=name
        self.des=des
        self.cl=cl
    def login(self):
        print("Login Completed "+self.name)
    def cla_check(self):
        if(self.cl=='CSE3'):
            print("Your class has a strength of 65")
        else:
            print("Sorry...,I don't Know about your class")
object=register("Sonia","Student","CSE3")
print(object.name)
print(object.des)
print(object.cl)
object.login()
object.cla_check()
