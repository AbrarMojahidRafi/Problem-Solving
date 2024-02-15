X = input()

ans = ""

if X[0] == "-":
  ans += "-"
else: 
  ans += "+" 
# print(ans)
def integer(ans):
  # print(ans)
  if "-" not in ans: 
    ans = ans + X[0] + "." 
    for i in range(1, 5):
      ans += X[i] 
    ans = ans + "E" + "+" + str(len(X)-1)    
    return ans
  else:
    ans = ans + X[1] + "." 
    for i in range(2, 6):
      ans += X[i] 
    ans = ans + "E" + "+" + str(len(X)-2)    
    return ans
  
def point(ans):
  
  pass 

if "." in X:
  print(point(ans))
else: 
  print(integer(ans))
