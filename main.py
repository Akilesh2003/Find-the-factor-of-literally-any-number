def print_factors(x):
  print("The factors of",x,"are:")
  for i in range(1, x + 1):
    if x % i == 0:
      print(i)
  return

num = int(input("Hello! Please enter the number whose factors you want to find: "))

print_factors(num)