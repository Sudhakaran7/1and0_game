a=list(map(str,input().split()))
n,k=map(int,input().split())
count=0
res=[]
for i in range(len(a)):
  if(len(a[i])<=n):
    count+=1
  else:
    res.append(a[i])
for j in range(len(res)):
  if(len(res[j])<=k):
    count+=1
print(count)
