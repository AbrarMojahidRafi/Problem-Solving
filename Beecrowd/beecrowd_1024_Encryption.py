N = int(input())
for i in range(N):
  user_input = input()
  s = ""
  for i in user_input: 
    if "a" <= i <= "z" or "A" <= i <= "Z": 
      s = s + chr(ord(i) + 3)
    else: 
      s = s + i
  # print(s)
  if len(s)%2 == 0:
    temp = ""
    for i in range(len(s)//2): 
      temp = temp + chr(ord(s[i]) - 1)
    temp = temp + s[i+1::]
  else: 
    temp = "" 
    for i in range(len(s)//2+1): 
      temp = temp + chr(ord(s[i]) - 1)
    temp = temp + s[i+1::]
  # print(temp)
  print(temp[::-1])
  