'''
Author: Yurii Bielotsytsia
Version: Easy-01
Name: Ideal BMI by Brok formula
'''
sex = input('Enter you sex(m if you are a man, w if you are a woman): ')
height = float(input('Enter you height in cm '))
if(sex == 'm'):
    result=(((height*4/2.54)-128)*0.453)
    print('You ideal BMI is {0:.2f}'.format(result))
elif(sex == 'w'):
    result=(((height*3.5/2.54)-108)*0.453)
    print('You ideal BMI is {0:.2f}'.format(result))
else:
    print('Error: you entered not valid sex')
