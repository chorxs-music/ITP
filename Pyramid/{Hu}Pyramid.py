stacks = int(input("Enter a pyramid value between 1 ~ 8: "))

for i in range(stacks):
  for k in range(stacks):
    if k > i:
      print(' ', end='')
  for j in range(stacks):
    if j <= i:
      print("#", end='')
  print()