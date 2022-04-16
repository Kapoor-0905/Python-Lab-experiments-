#Q1
#WAP to enter a string and a substring
def count_str(string,substring):
    count = 0
    for i in range(len(string)-len(substring)+1):
        if(string[i:i+len(substring)] == substring):
            count += 1
    return count
if  __name__ == '__main__':
    string = input().strip()
    substring = input().strip()
    count = count_str(string,substring)
    print(count)
    
#-------------------------------------------------------------------------------

#Q2
#WAP to input the first name, middle name and last name of a person and print first and middle name initals sperated with dot and last name with a space and dot

def shrt_name():
    fname = str(input("Enter the first name: "))
    mname = str(input("Enter the middle name: "))
    lname = str(input("Enter the last name: "))
    print("The Full name is: ", fname.capitalize(), mname.capitalize(), lname.capitalize())
    print("Please confirm your credentials....\n")
    c = str(input("To confirm your credentials enter 'CONFIRM'......\n"))
    if (c == "CONFIRM"):
        fname_i = fname[0]
        mname_i = mname[0]
        return "The shortened name is: "+fname_i.capitalize()+'.'+mname_i.capitalize()+'. '+lname.capitalize()
    else:
        print(shrt_name())
x = str(input("Enter 'sn' to short your name......."))
if(x == 'sn'):
    print(shrt_name())
else:
    print("Get this man a long name !!!")
#-------------------------------------------------------------------------------

#input a string with upper and lower case letters and print their occurence (case insensitve)

str1 =  str(input("Enter a string"))
count={}
str2=str1.upper()
for i in str2:
    count[i] = str2.count(i)
for j in count.keys():
    print(str(count[j])+j)

