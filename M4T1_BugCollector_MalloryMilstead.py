# Using a running total
# 6/25/2017
# CTI-110 M4T1 - Bug Collector
# Mallory Milstead

#Write a program that counts how many bugs were collected over a course of 5 days.

# Initialize the accumulator.
total=0

#Get the bugs collected for each day.
for day in range(1, 6):
    print('Enter the bugs collected on day', day)

#Input the number of bugs.
    bugs = int(input())

#Add bugs to total.
    total += bugs

#Display the total bugs.
print('You collected a total of', total, 'bugs.')
    
    
