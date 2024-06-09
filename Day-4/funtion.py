
#using function

num3 = 30
num4 = 50

def addition():  #def stand for function
    add = num3 + num4
    print(add)

def subs():      #def stand for function
    sub = num3 - num4
    print(sub) 

addition()   #invoke function
subs()       #invoke function

#function with return

def multiplication(num3, num4):
    m = num3 * num4
    return m

print(multiplication(3,5))
