mylist=[]
n=int(input("Enter no. of list element:"))
for i in range(0,n):
    elements=int(input("Enter list element:"))
    mylist.append(elements)

def max_min(mylist):
    max=mylist[0]
    min=mylist[0]
    for num in mylist:
        if num>max:
            max=num
        elif num<min:
            min=num
    return max,min

print("max and min numbers are:",max_min(mylist)," respectively.")