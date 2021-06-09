from itertools import groupby
n=int(input('How many Numbers'))
N = []
for k in range(n):

    a=int(input("Enter the numbers"))
    N.append(a)  
    N.sort()
    print([list(j) for i, j in groupby(N)])
print('Captain:',N[-1])
