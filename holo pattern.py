#n=int(input("enter the n"))
#for i in range(1,n+1):
 #   if i==1 or i==n:print("* "*n)
  #  else:print("*","   ","*")




n=int(input("enter the n"))
for i in range(1,n+1):
    if i==1 or i==n:print("* "*n)
    else:print("* ","  "*(n-3),"* ")
