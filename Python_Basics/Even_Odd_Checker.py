def odd_even(n):
  if n % 2 == 0:
    return "Even"
  else:
    return "Odd"
  
def print_result(n):
  result = odd_even(n)
  print(f"The result of this is {result}")
  
print_result(4)