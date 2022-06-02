A=['A','B','C','D','E']
n=3    #n times left shift
x=0
while x<n:
    #------------------------right shift
    # i=len(A)-1
    # while i>0:
    #     A[i]=A[i-1]
    #     i-=1
    # A[i]=0
    #------------------------right shift
    #------------------------left shift
    i=0
    while i<len(A)-1:
        A[i]=A[i+1]
        i+=1
    A[i]=0
    #------------------------left shift
    x+=1

print(A)