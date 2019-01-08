n=int(input())
re=0
m=n
while n>0:
   r=n%10
   re=re+(r*r*r)
   n=n//10
if m==re:
   print("yes")
else:
   print("no")
   
