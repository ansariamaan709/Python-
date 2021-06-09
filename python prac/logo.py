import collections
string=input().lower()
f={}
for i in string:
  f[i]=f.get(i,0)+1
print(f)
f=list(f)
print(f)
a_list =list(input().lower())
a_counter = collections.Counter(a_list)
most_common = a_counter.most_common(2)
print(most_common)