# Loop->While and for loop

#for loop run till the range run
for i in range(20):
    print(i)

for i in range(1, 10):
    print(i)

for i in range(1, 10, 2):
    print(i)

#for 
for i in range(0,20):
    if i%2==0:
        print(i,'even')

#for
for i in ['one','two','three']:
    if i=='two':
        print(i,'found')
        break
    else:
        print('not found')

# while loop 
# #while loop run till getting the condition false
i = 0
n = 10

while i < n:
    if i == 7:
        print(i)
    print("not found")
    i = i+1
    break



