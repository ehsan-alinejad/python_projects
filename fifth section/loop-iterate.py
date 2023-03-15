# mydict={'ehsan':22,'ali':30,'mohsen':24}
mydict={}
i=0
while True:
    name=input('name: ')
    age=int(input('age: '))
    mydict[name]=age
    contin=input('continue?(y/n) ')
    if contin =='n':
        break
print(mydict)

