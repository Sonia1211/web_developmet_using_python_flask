def demo():
    print("Welcome to Flask Introduction")
demo()
'''Function with parameters'''
def demo(name="Sonia"):
    print("welcome"+name)
demo()
#you can give name default or as parameter also...,Now you see the function with multiple parameters
def demo(age,name,des):
    print("age="+age)
    print("name="+name)
    print("des="+des)
demo(name="Kalyan",age="24",des="Dev")

cars=['benz','wagon','bajaj','maruthui']
def list_values(li):
    for i in li:
        print(i)
list_values(cars)
lis=[{"name":"Benz","year":2002},{"name":"wagon","year":2017},{"name":"Maruthi","year":2002}]
def list_val(l):
    for i in range(0,len(l)):
        print(lis[i]["name"])
        print(lis[i]["year"])
list_val(lis)

def demo(list):
    print("Welcome"+list[1])
lee=["adas","dasdas","dasds"]
demo(lee)













