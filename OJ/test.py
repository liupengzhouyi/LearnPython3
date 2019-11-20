n=int(input())
a=list(map(int,input().strip().split(" ")))
i=0
j=n-1
sum1=a[0]
sum2=a[n-1]
res=[]
while i<j:
  if sum1<sum2:
    i =1 + i
    sum1+=a[i]
  elif sum1>sum2:
    j = j - 1
    sum2+=a[j]
  elif sum1 == sum2:
    res.append(sum1)
    i = i + 1
    j = j - 1
    sum1 += a[i]
    sum2 += a[j]
res=sorted(res)
if len(res)==0:
  print("0")
elif len(res)>0:
  print(res[-1])
