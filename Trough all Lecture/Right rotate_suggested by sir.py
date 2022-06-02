A=['A','B','C','D','E']

i=len(A)-1
value=A[i]
while i>0:
    A[i]=A[i-1]
    i-=1

A[i]=value
# print(i)
print(A)