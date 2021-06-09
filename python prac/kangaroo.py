c=int(input("How Many jumps "))
a=[]
n= int(input("Enter the  starting step  for Kangaroo1 "))
o=int(input("Enter the  step size for Kangaroo1 "))
p=o
for i in range(c):        
    
    l=n+o
    o=o+p
    a.append(l)
print(a)

b=[]
q= int(input("Enter the  starting step  for Kangaroo2 "))
r=int(input("Enter the  step size for Kangaroo2 "))
p=r
for i in range(c):        
    
    l=q+r
    r=r+p
    b.append(l)
print(b)
if (a[-1]==b[-1]):
    print("YES")
else:
    print("NO")