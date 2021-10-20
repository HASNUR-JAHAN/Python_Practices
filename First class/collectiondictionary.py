#dictionary-key value pair->key:value
d={"key1":"value1",2:10,3:10.50}
print(d)
print(d["key1"])

for i in d:
    print(i)

for i,j in d.items():
    print(i,j)

for i,j in d.items():
    if i=="key1":
       print(i,j)

#print value with key by get, we need to give the key in the get
print(d.get("key1"))

#nested item
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

print(students.get("171200019"))

student_info=students.get(input())
if student_info==None:
    print("no data")
else:
    print(student_info["name"],student_info["Department"])

#type casting
#v=int(input())
#v=int(v)
#v=float(v)

print(d.keys())
print(d.values())

d2={"key2":"value2"}
d.update(d2)
print(d)


