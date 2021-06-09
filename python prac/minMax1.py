n = int(input().strip())
print(n)
k = int(input().strip())
A = []
while len(A) < n:
	A.append(int(input().strip()))

# Solution
A = sorted(A, reverse=True)
answer = min(A[i]-A[i+k-1] for i in range(n-k+1))
print(answer)