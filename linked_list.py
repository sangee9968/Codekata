def del_first():
   head=l[1]
   del [l[0]]
   return l
def del_mid(key):
   for i in range(1,len(l)-1):
      if l[i][0]==key:
         l[i-1][1]=l[i][1]
         del[l[i]]
   return l 
def del_last():
   del [l[-1]]
   l[-1][1]=0
   return l
l=[[1,100],[2,200],[3,300],[4,400],[5,0]]
head=l[0]
m=del_first()
print(m)
n=del_mid(3)
print(n)
o=del_last()
print(o)
