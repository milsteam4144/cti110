# Write a program that determines lifestage by age
# 6/18/17
# CTI-110 M3HW1 - Age Classifier
# Mallory Milstead
#

# This program gets an age from the user and determines their lifestage.


#Get age from the user.
age = int(input('Enter your age:'))

#Determine their lifestage.
if age <= 1:
    print ('You are in infant.')
else:
    if age > 1 and age < 13:
        print ('You are a child')
    else:
        if age > 13 and age < 20:
            print ('You are a teenager.')
        else:
            if age >= 20:
                print ('You are an adult.')
                
