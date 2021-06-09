import pickle
l=[1,2,3,4,5]
demo='dogs'
out=open('demo','wb')
b = pickle.dump(l,out)
out.close()
print(b)
