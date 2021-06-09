n=int(input())
k=int(input())
l=sorted([int(input()) for _ in range(n)])
i=0
print(min([abs(l[i+k-1]-l[i]) for i in range(n-k+1)]))
print(l[i+k-1])