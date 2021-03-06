#Q1 
#Input two values from user where the first line contains N, the number of test cases.
#The next N lines contain the space separated values of a and b. Perform integer division and print a/b.
#Print the error code in the case of ZeroDivisionError or ValueError
---------------------------------------------------------------------------------------------------------------------
try:
    N = int(input("Enter the number of test cases: "))
    for i in range(0,N):
        a= int(input("Enter the first number: "))
        b= int(input("Enter the second number : "))
        print(a/b)
except ZeroDivisionError:
    print("Denominator cannot be zero")
except ValueError:
    print("Different value")
#----------------------------------------------------------------------------------------------------------------------
#Q2
#Rewrite the code to handle the exceptions raised. Print appropriate error messages wherever applicable.

try:
    mylist = [1,2,3,'4',5]
    sum = 0
    for i in range(0,len(mylist)):
        check = isinstance(mylist[i],str)
        if(check==True):
            raise ValueError
except:
    print("Cannot perform arithmetic operations on strings...")
#----------------------------------------------------------------------------------------------------------------------
#Q3
try:
    f = open("testfile1.txt","w")
    f.write('Jack said, "Hello Pune".')
    f.close()


    f1 = open("testfile2.txt","w") 
    f4= open("testfile1.txt","r")


    d = f.read()
    lst = []
    for i in range(0,len(d)):
        print(d[i],end="")
        lst.append(d[i])
        if(lst[i] == '\"'):
            lst[i] = '\\"'
            
    print("\n")
    text = "".join(lst)
    f1.write(text)
    f1.close()

    f1 = open("testfile2.txt","r")
    a = f1.read()
    print(a)

except (FileNotFoundError, IOError, IndexError, EOFError, ValueError,NameError):
        print("Check the error..")
---------------------------------------------------------------------------------------------------------------------
