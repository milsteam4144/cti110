# Calculating tax, tip and total price of a meal
# 6/11/2017
# CTI-110 M2HW2 - Tip Tax Total
# Mallory Milstead

#Get the amount paid for just the meal.
meal_price=float(input('What is the price of the meal?'))

#Calculate tip.
tip=meal_price*0.18

#Display the tip amount.
print('An 18 percent tip is $' , format(tip, '.2f'))

#Calculate a 7 percent sales tax.
tax=meal_price*0.07

#Display the tax amount.
print ('A 7 percent sales tax is $' , format (tax, '.2f'))

#Calculate the final total.
total=meal_price+tip+tax

#Display the final total of the meal with tax and tip.
print ('The final total of the meal with tax and tip is $' , format (total, '.2f'))

