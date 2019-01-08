n=int(input())
rev=0
m=n
while n>0:
   r=n%10
   rev=rev+(r*r*r)
   n=n//10
if m==rev:
   print("yes")
else:
   print("no")
   
