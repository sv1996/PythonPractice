def oddsums(n):
  total=0
  result=[]
  for i in range(1,n+1):
    odd= 2*i-1
    total=total+odd
    result.append(total)
  return result