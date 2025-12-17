temprature=float(input('enter the temprature'))
x=chr(input('if it is c or f'))
if(x==c):
    f= (temprature*9/5)+32
    print('the result is in f')
elif(x==f):
    c=(temprature-32)*5/9
    print('the result is in c')
else:
    print ('invalid selection')