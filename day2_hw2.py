#Finding greatest element in a list using for loop
list1 = eval(input("Enter a list: "))

max = 0

for i in range(len(list1)):
  if list1[i]>max:
    max = list1[i]
  else:
    continue  

print(f"Largest element in {list1} is {max}")