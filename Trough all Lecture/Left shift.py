A=['A','B','C','D','E']

i=0
while i<len(A)-1:
    A[i]=A[i+1]
    i+=1

A[i]=0
# print(i)
print(A)