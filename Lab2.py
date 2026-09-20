#LAB2 Iterative structures,Functions,and 
# Classes/Objects in Python


#1.While loop
count=0
while count<3:
    count=count+1
    print("Hello")
#2.single statement while block
count=0
while count==0:
    print("Hello")
    break
#3.For loop list iteration
print("list iteration")
l=["geeks" ,"for" ,"geeks"]

for i in l:
    print(i)
#4.for loop string iteration
print("\nString iteration")
s="geeks"

for i in s:
    print(i)
#5.For loop tuple iteration
print("\ntuple iteration")
t=("geeks" ,"for" ,"geeks")

for i in t:
    print(i)
#6.Iterating by index
items=["geeks" ,"for" ,"geeks"]

for index in range(len(items)):
    print(items[index])
#7.Continue statement
for letter in "geeksforgeeks":
    if letter == "e"or letter == "s":
     continue
print("current letter:",letter)
#8.Break statement
for letter in "geeksforgeeks":
    if letter == "e" or letter == "s":
        break
    print("current letter:",letter)
#9.creating a function
def my_function():
    print("Hello from a function")
#10.calling a function
def my_function():
    print("Hello from a function")
my_function()
#11.Function with a parameter
def my_function(fname):
    print(fname + "refsnes")

my_function("emil")
my_function("tobias")
my_function("linus")
#12.Default parameter value
def my_function(country="Norway"):
    print("I am from" + country)

my_function("Sweden")
my_function("Pakistan")
my_function()
my_function("Brazil")
#13.Passing a list as a parameter
def my_function(food):
    for x in food:
        print(x)

fruits=["apple" ,"banana" ,"cherry"]
my_function(fruits)
#14.Return values
def my_function(x):
    return 5 * x
print(my_function(3))
print(my_function(5))
print(my_function(9))
#15.Keyword arguments
def my_function(child3, child2, child1):
    print("the youngest child is " + child3)

my_function(child1="emil" , child2="taha" , child3="lira")
#16.Creating a class
class Myclass:
    x=5
#17.Creating an object
class Myclass:
    x=5

p1=Myclass()
print(p1.x)
#18._init_()function and object properties
class person:
    def __init__(self , name , age):
        self.name=name
        self.age=age

p1= person("john" , 36)

print(p1.name)
print(p1.age)
#19.Object method
class person:
    def __init__(self , name , age):
        self.name=name
        self.age=age

    def myfunc(self):
        print("Hello my name is " + self.name)

p1= person("john" , 36)
p1.myfunc()