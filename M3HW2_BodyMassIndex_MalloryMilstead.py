# Chapter 3 Exercise #14
# 6/18/17
# CTI-110 M3HW2 - Body Mass Index
# Mallory Milstead
#     

#Get height and weight from user.
height = int(input('Enter your height:'))
weight = int(input('Enter your weight:'))

#Calculate BMI.
BMI = weight * (703 / height**2)

#Display BMI.
print('Your BMI is', format(BMI, '.1f'))

#Determine whether the user in under, optimal or over weight.
if BMI < 18.5:
    print('You are underweight.')
else:
    if BMI >= 18.5 and BMI <=25:
        print('You are optimal weight.')
    else:
        if BMI >25:
            print('You are overweight.')
            
            

