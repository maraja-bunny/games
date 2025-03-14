unit=input("Is this temperature in celcius or fahrenheit(c/f:)")
temp=float(input('enter the temperature:'))
if unit=="c":
    temp=round((9*temp)/5+32 ,1)
    print(f'the temperature in fahrenheit is:{temp}f')
elif unit=='f':
    temp=round((temp-32)*5/9,1)
    print(f'the temperature in celciusis:{temp}c')
else:
    print(f'{unit} is an ivalid unit of measurement')