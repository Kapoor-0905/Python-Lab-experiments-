
#Given an integer n, perform the following conditional actions:
# If n is odd, print Weird
# If n is even and in the inclusive range of 2 to 5 , print Not Weird
# If n is even and in the inclusive range of 6 to 20, print Weird
# If n is even and greater than 20, print Not Weird

num=int(input("Enter number of looping : "))
for i in range(0,num):
    num1 = int(input("Enter any number: "))
    if (num1%2!=0):
        print("Weird")
    if (num1%2==0 and (num1>=2 and num1<=5)):
        print("not weird")
    elif (num1%2==0 and (num1>=6 and num1<=20)):
          print("Weird")
    elif(num1%2==0 and (num1>20 )):
        print("not weird")

#---------------------------------------------------------------------------------------------------------

#WAP to read an integer ‘n’ from STDIN. For all non-negative integers i<n, print i2 on a separate line


num1 = int(input("Enter any number: "))
if(num1<0):
    print("no negative numbers allowed...")
else:
    for i in range(1,num1):
        print(i*i)

#---------------------------------------------------------------------------------------------------------

#3. WAP to read an integer from STDIN. Without using any string methods, print the following on a sible line


num1 = int(input("Enter any number: "))
if(num1<0):
    print("no negative numbers allowed...")
else:
    for i in range(1,num1+1):
        print(i,end="")
