T = int(input())
for _ in range(T):
  X = int(input())
  cost = X * 4 
  if cost <= 1000:
    print("Yes")
  else: 
    print("No")