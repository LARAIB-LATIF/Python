print('hello friend')
list=['a,b,c']
print(list)
print("Cheers, Mate!")
x = 4
y = "jack"
print(x)
print(y)
thislist =["1","2","3"]
print(thislist)
thislist=["4","6","4","8"]
print(thislist)
thislist=["apple","banana","strawberry"]
print(len(thislist))
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]
print(list1,list2,list3)
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]
print(list1,list2,list3)
thislist=["apple","banana","strawberry"]
print(thislist[1])
thislist=["apple","banana","charry"]
print(thislist[-2])
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:3])
thislist = ["orange", "kiwi", "melon", "mango"]
print(thislist[:2])
thislist = ["banana", "cherry", "orange", "kiwi", "mango"]
print(thislist[2:])
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon"]
print(thislist[-3:-1])
thislist = ["apple", "banana", "cherry"]
if "banana" in thislist:
    print("Yes, 'banana' is in the fruits list")
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)
thislist = ["apple", "banana","cherry"]
thislist.append("bluebarry")
print(thislist)
thislist = ["marker", "pencil", "pen"]
thislist.insert(1, "ballpen")
print(thislist)
thislist = ["red", "blue", "yellow"]
for i in range(len(thislist)):
    print(thislist[i])
thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)
thislist = ["bag", "shoes", "clothes", ]
thislist.sort(reverse = True)
print(thislist)
thislist = ["notebook", "dairy", "book"]
mylist = thislist.copy()
print(mylist)
list1 = ["p", "q", "r"]
list2 = [2, 4, 6]
list3 = list1 + list2
print(list3)
list1 = ["e", "f" , "g"]
list2 = [6,7,8]
list1.extend(list2)
print(list1)
list1 = ["x", "y" , "z"]
list2 = [4, 5, 6]
for x in list2:
    list1.append(x)
print(list1)
