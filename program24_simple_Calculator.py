num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))
def add(num1,num2):
    return num1+num2
def subract(num1,num2):
    return num1-num2
def multiply(num1,num2):
    return num1 * num2
def divide(num1,num2):
    return num1/num2
print(''' The list of operations are:
1) Add
2) Subract
3) Multiply
4) Divide

Please enter your prefered operation by entering that choice number:
'''
)
select=int(input("Enter operation number 1,2,3 or 4 :"))
if select==1:
    print(f"{num1}+{num2} =",add(num1,num2))
elif select==2:
    print(f"{num1}-{num2} =",subract(num1,num2))
elif select==3:
    print(f"{num1}*{num2} =",multiply(num1,num2))
elif select==4:
    print(f"{num1}/{num2} =",divide(num1,num2))
else:
    print("No valid operation selected")
