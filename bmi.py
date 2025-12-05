print('enter your height and weight:')
weight=float(input('enter your weight in kg:'))
height=float(input('enter your height in cm:'))
height=height/100
BMI=weight/(height*height)
print(BMI)