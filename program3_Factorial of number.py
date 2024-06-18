# num=int(input("Enter number for factorial :"))

# def factorial(num):
#     if num==1 or num==0:
#         return 1
#     else :
#         num=num*factorial(num-1)
    
# print(f"Factorial of {num} is:", num)





num=int(input("Enter number: "))
## f is factorial
f=1
if num==0:
    f=f*num
elif num==1:
    f=f*num
elif (num!=0 or num!=1):
    for i in range(num+1) :
        if(i==0):
            continue
        f=f*i
        # print(i)
        i=i-1
        # print(i)
    
print(f"factorial of {num} is:",f)
    