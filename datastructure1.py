set1={1,2,3,4,5,6,7,8,9,10}
list1=list(set1)
list1.insert(0,list1[4])
list1.insert(1,list1[4])
list1.insert(2,list1[7])
list1.insert(3,list1[9])
list1.insert(6,list1[1])
list1.insert(7,list1[2])
list1[8:10]=list1[12:14]
list1[10:]=[]
print(list1)
print(list1[3:6])
set2=set(list1)
print(set2)
del set2
str1='python is powerful'
list2=list(str1)
print(list2)
