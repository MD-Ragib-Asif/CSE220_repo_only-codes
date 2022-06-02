A=['A','B','C','D','E']

i=len(A)-1
while i>0:
    A[i]=A[i-1]
    i-=1

A[i]=0
# print(i)
print(A)