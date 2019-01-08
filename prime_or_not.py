n=int(input())
for i in range(2,n):
   if n%i==0:
      flag=0
      break
   else: 
      flag=1
if flag==0:
   print("no")
else:
   print("yes")
