# Python Queue Simulation - Sophia Ramirez Velandia

# Initializing a queue
names= []

n= 10
for i in range (n):
    name= input("Enter name: ")


# Adding elements to the queue
names.append('Joe')
names.append('Sally')
names.append('Jim')
names.append('June')
names.append('Betty')
names.append('Bill')
names.append('Sara')
names.append('Zak')
names.append('Anne')
names.append('Kate')

print(names)
             

# Second loop using length of a list
names = ['Joe', 'Sally', 'Jim', 'June', 'Betty', 'Bill', 'Sara', 'Zak', 'Anne', 'Kate']
for x in range (len(names)):
    print(names.pop(0))
print(names)
