#data structure
#colletion-list

list_val = [1, 2, 5, 40, 40.05, 'seven', 'nine']
print(list_val)
print(type(list_val))

for i in list_val:
    print(i)
    print(type(i))

# indexing

print(list_val[2])

# Slicling
print(list_val[2:5])
print(list_val[4:])
print(list_val[:4])
print(list_val[-1])
print(list_val[::-1])  # revirse

# List mutable(changable item) collection
print(list_val)
list_val[0] = 10000
print(list_val)

# re assign
list_val = list_val+["Anika"]
print(list_val)

#built a function
list_val.append(200)
print(list_val)

# Reversel
list_val.reverse()
print(list_val)

#POP
take = list_val.pop()
print(list_val)
print(take)

#count
print(list_val.count(2))

# Comprehension
list_comp = [i for i in range(10)]
print(list_comp)

#nested item
nested_list=[[1,2,3],[4,5,6],[7,8,9]]
print(nested_list[0])
print(nested_list[0][1])

# (tupple,set) immutable(changable na)
