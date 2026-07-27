no=int(input("enter a number"))
s=0
temp=no

while no>0:
    r=no%10
    s=s+r
    if no>9:
    	s=s*10
    no=no//10
if temp==s:
    print("its palindrome")
else:
    print("its not a Palindrome")
    

#no=121
#r=121%10=1
#s=0+1=1
#s=1*10=10
#no=121//10=12


#no=12
#r=12%10=2
#s=10+2=12
#s=12*10=120
#no=12//10=1

#no=1
#r=1%10=1
#s=120+1=121
#no=1//10=0
