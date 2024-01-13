D, N = map(str, input().split(" "))

if int(D) != 0: 
  s = ""
  for i in N: 
    if i != D: 
      s = s + i 
  
  try: 
    if int(s) == 0:
      print(0)
    else: 
      print(int(s))
  except: 
    print(1)
else: 
  print()
  