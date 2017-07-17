# A brief description of the project
#6/30/2017
#CTI-110 M5HW1 - Test Average and Grade
# Mallory Milstead
#

#Constant for the number of test scores.
NUMBER_OF_SCORES = 5


score1 = int(input('Enter the first test score: '))
score2 = int(input('Enter the second test score:'))
score3 = int(input('Enter the third test score: '))
score4 = int(input('Enter the fourth test score:'))
score5 = int(input('Enter the fifth test score: '))




#This program will obtain 5 test scores from the user and determine each score's
#letter grade and the average of all 5 scores.


def determine_grade():
#Get the test scores as constants.
#Get first score and letter grade.
        if score1 >=90:
                print('Score 1 is an A.')
        if score1>=80 and score1<= 89:
                print('Score 1 is a B.')
        if score1 >=70 and score1<= 79:
                print('Score 1 is a C.')
        if score1>=60 and score1<= 69:
                print('Score 1 is a D.')
        if score1 < 60:
                print('Score 1 is an F.')
    

#Get second scoreand letter grade.
        
        if score2 >=90:
                print('Score 2 is an A.')
        if score2 >=80 and score2<= 89:
                print('Score 2 is a B.')
        if score2 >=70 and score2<= 79:
                print('Score 2 is a C.')
        if score2 >=60 and score2<= 69:
                print('Score 2 is a D.')
        if score2 < 60:
                print('Score 2 is an F.')

#Get third scoreand letter grade.
        
        if score3 >=90:
                print('Score 3 in an A.')
        if score3 >=80 and score3<= 89:
                print('Score 3 is a B.')
        if score3 >=70 and score3<= 79:
                print('Score 3 is a C.')
        if score3 >=60 and score3<= 69:
                print('Score 3 is a D.')
        if score3 < 60:
                print('Score 3 is an F.')

#Get fourth score and letter grade.
        
        if score4 >=90:
                print('Score 4 is an A.')
        if score4 >=80 and score4<= 89:
                print('Score 4 is a B.')
        if score4 >=70 and score4<= 79:
                print('Score 4 is a C.')
        if score4 >=60 and score4<= 69:
                print('Score 4 is a D.')
        if score4 < 60:
                print('Score 4 is an F.')

#Get fifth score and letter grade.
        
        if score5 >=90:
                print('Score 5 is an A.')
        if score5 >=80 and score5<= 89:
                print('Score 5 is a B.')
        if score5 >=70 and score5<= 79:
                print('Score 5 is a C.')
        if score5 >=60 and score5<= 69:
                print('Score 5 is a D.')
        if score5 < 60:
                print('Score 5 is an F.')


    
def calc_average():
    #Get the average of test scores.
    average = (score1 + score2 + score3 + score4 + score5) / NUMBER_OF_SCORES
    #Print the average
    print('The average grade for the test scores is', average)
    if average >=90:
        print('The average in an A.')
    if average >=80 and average <= 89:
        print('The average is a B.')
    if average >=70 and average <= 79:
        print('The average is a C.')
    if average >=60 and average <= 69:
        print('The average is a D.')
    if average < 60:
        print('The average is an F.')


#Execute functions.
determine_grade()
calc_average()


    
