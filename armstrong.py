h=int(input())
re=0
m=n
while h>0:
   r=h%10
   re=re+(r*r*r)
   h=h//10
if m==re:
   print("yes")
else:
   print("no")
   
