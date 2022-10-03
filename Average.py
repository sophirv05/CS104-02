#Sophia Ramirez Velandia

howMany = int(input("How many test scores would you like to average? "))

#Set average to 0
average = 0
#Set total to 0
total = 0
#Set howManyEntered to 0
howManyEntered = 0


while howManyEntered < howMany:
    testScore = int(input("Enter test score: "))
    total += testScore
    howManyEntered +=1


average = (total / howManyEntered)

print("The average for the test scores you entered is: ", average)

