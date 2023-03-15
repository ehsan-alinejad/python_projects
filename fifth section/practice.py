list=[]
result=0
while True:
    num=input('enter number or =:(num/=) ')
    if num =='=':
        break
    else:
        result=result+float(num);
        list.append(num)
print('jam adad vared shode=',result)
print('------------------')
count=0
while count<len(list):
    print(count+1,'ehsan')
    count+=1;
