s=""
n,k=map(int,input().strip().split())
for i in range(n+1,k):
      if i%2==0:
         s=s+str(i)+" "
w=s.strip()
print(w)
