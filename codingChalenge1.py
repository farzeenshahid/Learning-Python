#Calculate simple interest
#Formula ---> SI = (Prinipal * rate of interest * Time)/100
P = int(input("Enter Pricipal: "))              
#this could also be written as -->  p = input('Enter value of P:')
# p = int(p)
r = int(input("Enter rate of interest: "))
T = int(input("Enter Time: "))
SI = (P * r * T)/100
print("Simple interest is " , SI)

