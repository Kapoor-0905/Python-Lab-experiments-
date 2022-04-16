#Q1
#fibonacci series

def fibo(n):
    a=0
    b=1
    for i in range(1,n+1):
        num1=a+b
        a=b
        b=num1
        print(a)

fib = str(input("press 'f' to print fibonacci series...."))
if (fib=='f'):
    num=int(input("Enter the nukmber of terms: "))
    print(fibo(num))
else:
    print("wrong call")

#----------------------------------------------------------------------------------------------------    
#Q2
#Write a Python program to find the maximum and minimum values in a given list of tuples using
#lambda function.


def traveller(name,ID):
    return name, ID
def baggage_check(weight):
    if(weight>0 and weight<=40):
        return True
    else:
        return False
def check_immigration(year):
    if(year>=2030 and year<=2050):
        return True
    else:
        return False
def check_security(noc):
    if(noc=='valid' or noc=='VALID'):
        return True
    else:
        return False

call = str(input("Press 'T' to enter traveller info....."))
if(call=='T'):
    Name=str(input("Enter the name: "))
    t_id=int(input("Enter the traveller id: "))
    print(traveller(Name,t_id))

    bw=str(input("Press 'BW' to check baggage weight......"))
    if(bw=='BW'):
        w=int(input("Enter the weight of bag: "))
        print(baggage_check(w))
    else:
        print("Wrong Call")

    yr=str(input("press 'CI' to check immigration year...."))
    if(yr=='CI'):
        yer=int(input("Enter the immiggration year: "))
        print(check_immigration(yer))
    else:
        print("Wrong Call")

    secu = str(input("Press 'S' for security check...."))
    if(secu=='S'):
        noc_c=str(input("Enter the vailidity: "))
        print(check_security(noc_c))
    else:
        print("Wrong call")
else:
    print("wrong call")

if(baggage_check(w)== True) and (check_immigration(yer)==True) and (check_security(noc_c)==True):
    print("Name is: ",Name)
    print("Travelling ID is: ",t_id)
    print("Allowed to fly!!")
else:
    print("Name is: ",Name)
    print("Travelling ID is: ",t_id)
    print("detained for teavelling")
Call=str(input("Press 'CONTINUE' to call the function again..."))
if(Call=='CONTINUE'):
    print(traveller(a,b))
else:
    print("End of program")
    
#-----------------------------------------------------------------------------------------------------------------

#Q3
List = [('V', 62), ('VI', 68), ('VII', 72), ('VIII', 70), ('IX', 74), ('X', 65)]
print("The original List is: ",List)
max_val = max(List,key = lambda a: a[1])[1]
min_val= min(List, key = lambda b: b[1])[1]
print(max_val , min_val)
