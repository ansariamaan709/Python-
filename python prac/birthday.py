n= int(input("how many candles"))
a=[]
for i in range(n):
    b=int(input("Enter the size of candles"))
    a.append(b)
c=a.count(max(a))
print("The candle blown is :" , c)

