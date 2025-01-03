number = 13200
reversed = number
while number!=0:
 remainder=number %10
 number = number / 10
 reversed = (reversed * 10) + remainder

print(reversed)
  