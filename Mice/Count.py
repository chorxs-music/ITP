count = 0
while (count < 3):
    count = count + 1
    print("Happy Birthday!")
    
for i in range(128):
    print(f"The next MIDI note value is {i}")
    
for i in range(76, 127, 2):
    print(f"The next MIDI note value is {i}")
    
for i in range(10):
  for j in range(10):
    if j >= i:
      print(j, end='')
  print()