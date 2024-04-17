mylist = ["apple" , 3 , True , "apple"]
print(mylist)
#accessing by index. Index starts from 0.
print(mylist[1])
#negative index starts from -1 which is last otem in the list
print(mylist[-1])
#Changing value at a specified index
mylist[2] = False
print(mylist)
#checking if omthings is available in a list
print("Bananas" in mylist)
print("apple" in mylist)
newlist = ["Toyota" , "kiwi" , "brazil" , True , 55]
#defining ranges in list. Note it will print from 1-3 4th position won't be printed
print(newlist[1:4])
#add items to list
mylist.insert(2,"trpies")
print(mylist)
mylist.append("shop")
#extending list by combining 2 lists
mylist.extend(newlist)
print(mylist)
#remove items from list
newlist.remove("kiwi")
print(newlist)
#removes specified index
newlist.pop(1)
print(newlist)
#clear all items of list
newlist.clear()
print(newlist)
#Looping through list --- for loop ---
list1 = ["Siri","alexa","bard"]
for x in list1:
    print(x)
#or loop by index number
for i in range(len(list1)):
    print(list1[i])
# while loop
i = 0
while i<len(list1):
    print(list1[i])
    i += 1
#list comprehension ---> shorter way of creating new list based on values of some existing list.
#consist of short form of a for loop and a conditional.
makeup = ["foundation" , "concealer" , "eyeshadow" , "blush" , "mascarra" , "eye liner" , "lipstick"]
makeupExclusive = [x for x in makeup if "a" in x]
print(makeupExclusive)
oddNos = [x for x in range(20) if x%2]
print(oddNos)
#sorting list in alphanumerical ascending order
makeup.sort()
print(makeup)
#sorting in descending order
oddNos.sort(reverse= True)
print(oddNos)
#sorting is case sensitive
list1.sort()
print(list1)
list1.sort( key = str.lower)
print(list1)
#reverse a list
list1.reverse()
print(list1)
# making copies of list 2 methods
copylist = makeupExclusive.copy()
print(copylist)
# or
newcopy = list(makeupExclusive)
print(newcopy)
# creating list with ranges
list2 = list(range(10))
print(list2)
list3 = list(range(1,15))
print(list3)
#list with intervals
intervalList = list(range(0,30,3))
print(intervalList)