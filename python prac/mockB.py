n=input('Enter the digits')
output=list(map(int,str(n)))
print(output)
a=max(output)*11+min(output)*7
print(a)
x=len(str(a))
output1=list(map(int,str(a)))
print(output1)
if x>2:
    y=output1.pop(0)
    print(y)
    print(output1)