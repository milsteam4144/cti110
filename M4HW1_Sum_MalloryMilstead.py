# Using a running total and condition-controlled loop
# 6/25/2017
# CTI-110 M4HW1 - Sum of Numbers
# Mallory Milstead
#

#This program calculates the sum of a series of numbers that the user enters.
#The series is ended when a negative number is entered.

#Initialize an accumulator variable.
total = 0
#Explain program to user.
print('Please enter a series of positive numbers. In order to end the series, enter a negative number.')

#Get the first number.
number = int(input('Enter a positive number:'))

#Continue processing as long as the user does not enter a negative number.
while number > 0:
      total = total + number

      print('Enter the next positive number or enter a negative number to end.')
      number= int(input())

#Once a negative number is entered, the loop ends and the total of all positive numbers is displayed.
print('The total of all positive numbers is:', total)
      



      


                       
