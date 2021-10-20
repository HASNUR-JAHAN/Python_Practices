students={
    "2297":{
        "name":"Hasnur Jahan",
        "Department":"SWE",
        "age":"23"
    },
    "2392":{
        "name":"Janatun Naima",
        "Department":"SWE",
        "age":"23"
    },
    "2406":{
        "name":"Anika Talukder",
        "Department":"SWE",
        "age":"23"
    },
    "171200019":{
        "name":"Mijanur Rahman",
        "Department":"BBA",
        "age":"25"
    }
}

def find_student(id):
    student_info=students.get(id)
    if student_info==None:
        print("no data")
    else:
        print(student_info["name"],student_info["Department"])

find_student("2297")

def get_name(name,name2,name3):
    print(name,name2,name3)

def get_num(num1,num2,num3):
    print(num1,num2,num3)

get_name("sorif","khan","amir")
get_num(10,20,30)

#number argument
def get_number(*number):
    print(number)
get_number(100,200,300,400,500)

#key word arguments(give after number argments)
def get_namess(*number,**name):
    print(number)
    print(name)
get_namess(1000,2900,3009,8400,6500,name="hasnur",age="23")

def mixed_arguments(nam,age,*number,**name):
    return nam+""+str(age)

print(mixed_arguments("shohel",35))

#print can storein variable
#return can not store in any variable