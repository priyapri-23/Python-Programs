num=input("Enter num: ")
def digitSum(num):
    sum=0
    for digit in str(num):
        sum +=int(digit)
    return sum
print(digitSum(num))