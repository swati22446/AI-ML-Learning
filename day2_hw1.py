#Factorial using while loop
num = int(input("Enter a number = "))

if num >=0 :
  num2 = num
  fact = 1
  while(num2 > 0):
    fact = fact*num2
    num2-=1
  print(f"Factorial of {num} = {fact}")
else:
  print("Cannot find factorial of a negative number")