names = ["Stacy" , "Kyle" , "Alice" , "Bruno"]
for x in names:
    print(x)
print("-----------------------------")
#break statement
for x in names:
    print(x)
    if x == "Alice":
        break
print("-----------------------------")
#placing break before printing name
for x in names:
    if x == "Alice":
        break
    print(x)
print("-----------------------------")
#else with for is executed after completion of for loop
for x in names:
    print(x)
else:
    print("List printed successfully")
print("-----------------------------")
#else with for loop while using break ---> else is not executed
for x in names:
    print(x)
    if x == "Alice":
        break
else:
    print("List printed successfully")
print("-----------------------------")
