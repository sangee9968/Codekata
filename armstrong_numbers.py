s=""
n,k=map(int,input().strip().split())
for i in range(n,k):
   rev=0
   temp=i
   while temp>0:
      r=temp%10
      rev=rev+(r*r*r)
      temp=temp//10
   if i==rev:
      s=s+str(i)+" "
w=s.strip()      
print(w)
