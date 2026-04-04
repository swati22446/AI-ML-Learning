def add(a , b):
  return a+b

def subtract(a , b):
  return a - b

def multiply(a , b):
  return a*b

def divide(a , b):
  if b != 0:
    return a/b
  else:
    return "Division ny zero is not allowed"
  
while True:
  print("\nMenu")
  print("1. Addition")
  print("2. Subtraction")
  print("3. Multipliation")
  print("4. Division")
  print("5. Exit")
  
  choice = int(input("Enter your choice: "))
  
  if choice == 5:
    print("Exiting Program")
    break
  
  num1 = float(input("Enter first number: "))
  num2 = float(input("Enter the second number: "))
  
  if choice == 1:
    print("Results:", add(num1 ,num2))
  elif choice == 2:
    print("Results:", subtract(num1 ,num2))
  elif choice == 3:
    print("Results:" , multiply(num1, num2))
  elif choice == 4:
    print("Results:", divide(num1 , num2))
  else:
    print("Invalid Input")