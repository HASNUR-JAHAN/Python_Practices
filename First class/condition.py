"""# Conditions
condition = True
if condition == True:
    print('Class will be held')
else:
    print('Not be happend')


#nested loop
age = 22
nid = 'Y'
if age >= 18:
    if nid == 'Y':
        print('you are able to give vote')
    else:
        print('Bring your NID')
else:
    print('Cant able to vote you are under 18')

# User Input/dynamic value
age = int(input('Enter Your Age ='))
if age >= 18:
    print('You are able to give vote')
    nid = input('do you have NID (Y/N) =')
    if nid == 'Y':
        print('Able to give vote')
    else:
        print('Bring your NID')
else:
    print('Cant able to vote you are under 18')"""


# Condition Ladder= check all condition till getting the right result
# ==, <=, >=, !=, or(|), and(&), not(!)
mark = int(input('Enter your mark = '))
if mark >= 0 and mark <= 39:
    print('Fail')
elif mark >= 40 and mark <= 79:
    print('Pass')
elif mark >= 80 and mark <= 100:
    print('Outstanding')
else:
    print('You must need to inpute your number')