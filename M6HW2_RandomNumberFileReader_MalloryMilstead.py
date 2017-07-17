# Write a program that can read a random number of numbers within a file
# 7/16/2017
# CTI-110 M6HW2 - Random Number File Reader
# Mallory Milstead
#

def main():
    

    #Open the random.txt file.
    random_file = open('random.txt', 'r')

    #Print opening line.
    print('The numbers in this file are:')

    #Read the first line and test for an empty string.
    line = random_file.readline()

    #As long as an empty string is not returned, continue processing.
    while line !='':
        #Convert line to a float.
        number = int(line)

        #Print the numbers from the file.
        print(format(number))

        #Read next line.
        line = random_file.readline()
    

    #Close the file.
    random_file.close()

    

def add():

    #Initialize an accumulator.
    total = 0

    

    #Open the random.txt file.
    random_file = open('random.txt', 'r')

        #Read values from file and accumulate them.
    for line in random_file:
        number = int(line)
        total += number

    #Close the file.
    random_file.close()

    #Print the total.
    print('The total of these numbers is:')
    print(format(total, 'd'))


def generations():

    #Initialize an accumulator.
    total = 0

    #Open the random.txt file.
    random_file = open('random.txt', 'r')

    #Read the number of values in this file.
    for line in random_file:
        number = 1
        total += number

    #Print the number of values in the file.
    print('There are', total, 'numbers in this file.')

main()
add()
generations()
input()







    


