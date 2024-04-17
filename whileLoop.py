#for while loop we have to set the counter first and then we have to increment it explicitly.
i = 0
while i<10:
    print(i)
    i+=1
else:
    print("i is no longer less than 10.")

#continue statement unline break statement won't come out of the loop instead it would do nothing 
#for that iteration and continue from next iteration.
i = 0
while i<10:
    i+=1
    if i == 7:
        continue
    print(i)
    