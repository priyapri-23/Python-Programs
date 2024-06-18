myList=[]
sum=0
n=int(input("Enter no. of list element:"))
for i in range(0,n):
    elements=int(input("Enter list element:"))
    myList.append(elements)

for i in range(0,n):
    sum=sum+myList[i]

print("sum of all list element:",sum)
