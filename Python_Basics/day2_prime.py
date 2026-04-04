import math
num = int(input("Enter a number = "))
s = int(math.sqrt(num))

if num > 1:
  for i in range(2 , s+1):
    if num % i == 0:
      print(f"{num} is not a prime number")
      break
  else:
    print(f"{num} is a prime number")
else:
  print(f"{num} is not a prime number")