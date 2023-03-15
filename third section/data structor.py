listt=[1,'a',3,4,8]
dictionary1={'name':'ehsan',
             'family':'alinejad'}
set1={'a','b','c'}
set2={'a','f','g'}
u=set1.union(set2)
dif=set1.difference(set2)
eshtrak=set1.intersection(set2)
tuple1 =('a','b')
word=input('word ro vared kond')
sdadar=['a','e','i','o','u']
found={}
for i in word:
    if i in sdadar:
        found.setdefault(i,0)
        found[i] += 1


for i in found:
    print(i,'tedadesh',found[i],'hast')

