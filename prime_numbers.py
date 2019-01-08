s=""
n,k=map(int,input().split())
for num in range(n+1,k):
   if num>1:
      for j in range(2,num):
         if num%j==0:
            break
      else:
         s=s+str(num)+" "
w=s.strip()
print(w)
