T = int(input())
for _ in range(T):
  N, X = map(int, input().split())
  s = f"{N*X}"
  if len(s) != 5: 
    print("NO")
  else:
    print("YES")