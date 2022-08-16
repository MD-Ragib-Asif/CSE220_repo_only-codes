#length_of_string recursive function

def length_of_string(s):

  if s == '':

    return 0

  else:

    return 1+length_of_string(s[1:])

print(length_of_string('hello'))


#sum of digits

def sum_of_digits(num,sum):

  if num == 0:

    return sum

  return sum_of_digits(int(num/10), sum+(num%10))

print(sum_of_digits(123,0))
