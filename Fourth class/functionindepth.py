#Function
def multiplication(number):
    result=number**2
    print(result)
multiplication(3)
print("*"*10)
#nested function
def first_func():
    def sec_func():
        print("this is an inner function")
    sec_func()
    print("this is an outer function") 

def outter_fun(name):
    def inner_func():
        print("welcome",name)

first_func()
outter_fun

#return process
def first_func():
    def sec_func():
        print("this is an inner function")
    print("this is an outer function")
    return sec_func()

def outter_fun(name):
    def inner_func():
        print("welcome",name)
    return inner_func()

first_func()
outter_fun("Anu")


#factorial
#exeption handling
def factorial(number):
    try:
        if not isinstance(number,int):
            raise TypeError("Sorry, number must be integer")
        if number <0:
            raise ValueError("Please input number mustbe bigger then zero")
    
        def cal_fact(num):
            if num<=1:
                return 1
            return num*cal_fact(num-1)

        return cal_fact(number)
    except ValueError as e:
        print(e)

print(factorial(6))

print("*"*10)

#lambda function-single line function(can write less in indepth)
#def num(x):
#  if x==10:
#     return x**3
#  else:
#    return x
numb=lambda x:x**3 if x==10 else x
print(numb(10))

another_lambda=lambda a,b:a+b if a==100 and b==200 else (b-a)
print(another_lambda(100,300))