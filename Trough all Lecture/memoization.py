#fibonacci series function

def fibonacci(num):

  if num == 0:

    return 0

  elif num == 1:

    return 1

  else:

    return (fibonacci(num-1)+fibonacci(num-2))

print(fibonacci(5))



#grid walking function

def grid_walk(m,n):

  if m<0 or n<0:

    return 0

  if m == 0 or n == 0:

    return 1

  else:

    return grid_walk(m-1,n)+grid_walk(m,n-1)

a=4

b=4

print(grid_walk(a,b))

#selection sort recursive function

def selection_sort(a,i,j):

  l=len(a)

  if i == l and j==l:

    return -1

  if i < l-1:

    min=i

    while j < l:

      if a[j] < a[min]:

        min = j

      j=j+1

    if min != i:

      temp=a[i]

      a[i]=a[min]

      a[min]=temp

    selection_sort(a,i+1,i+2)

A=[13,25,0,-4,7,-1,18,9,-6,21]

i=0

j=i+1

selection_sort(A,i,j)

print(A)

#insertion sort recursive function

def insertion_sort(a,i):

  l=len(a)

  if i == l:

    return -1

  if i < l:

    j=i-1

    key=a[i]

    while j>=0 and key<a[j]:

      a[j+1]=a[j]

      j=j-1

    a[j+1]=key

    insertion_sort(a,i+1)

#Tester

A=[22,5,14,2,7,1]

i=1

insertion_sort(A,i)

print(A)

