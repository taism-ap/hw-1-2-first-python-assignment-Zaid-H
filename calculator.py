print("I am your python calculator")
x= int(input("Please choose a number"))
y= int(input("Please choose a second number"))
z=input("Please choose a operation:+,-,/,*")
        
def s(x,y):
    return x-y
def a(x,y):
    return x+y
def m(x,y):
    return x*y
def d(x,y):
    return x/y

if z == '+':
    print(a(x,y))
if z == '-':
    print(s(x,y))
if z == '/':
    print(d(x,y))
if z == '*':
    print(m(x,y))
