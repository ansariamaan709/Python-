
n=2
d={map(str,input("Enter the letters").split()) for i in range(0,n)}
print(dict(d))
s=[]

z=input("Enter")
for i in range(0,n):
    y=input("Enter the string")
    s.append(y)
print(s)

if s in d:
    print("found")