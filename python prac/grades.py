a=[]
n=int(input("Enter how many numbers"))
for i in range(n):
    b=int(input("Enter the numbers"))
    a.append(b)
print(a)
for i in range(n):
    c=a[i]%5
    if (c<3):
        print(a[i])
    elif(c==3):
        a[i]=a[i]+2
        print(a[i])
    else:
        a[i]=a[i]+1
        print(a[i])
        



        
    

