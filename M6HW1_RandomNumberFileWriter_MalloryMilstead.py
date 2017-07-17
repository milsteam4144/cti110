# Write Random Numbers to a File
# 7/16/
# CTI-110 M6HW1 - Random Number File Writer
# Mallory Milstead
#
#This program will create a file called random.txt and write to it a series of
#random numbers 1-500. The user will decide how many random numbers are created
#and saved to the file.

#Import random function.
import random


def main():

    MIN = 1
    MAX = 500

    #Get input from user.
    howmany = int(input('How many random numbers would you like to generate?'))

    
    #Create and open the file.
    random_file = open('random.txt', 'w')


    #Write the numbers to the file.
    for count in range(howmany):
        random_file.write(str(random.randint(MIN, MAX)) + '\n')



    #Close the file.
    random_file.close()
    print('The numbers were written to random.txt')

#Call the main function.
main()
