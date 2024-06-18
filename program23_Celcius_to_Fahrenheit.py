s=input("Enter temperature degree to convert (celsius/fahrenheit):")
temp_value=int(input("Enter temperature:"))
def temp_conversion(s,temp_value):
    
    if s=='celsius':
        celsius=temp_value
        fahrenheit = (1.8 * celsius) + 32
        print("Temperature in Fahrenheit is:", fahrenheit)
    elif s=='fahrenheit':
        fahrenheit=temp_value
        celsius = ((fahrenheit-32)*5)/9
        print("Temperature in celcius is:", celsius)
    else:
        print("Invalid temperature input")


print(temp_conversion(s,temp_value))