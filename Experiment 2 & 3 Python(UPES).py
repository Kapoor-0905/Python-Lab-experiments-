#Q2

#WAP to input a list of scores for N students in a list data type. Find the score of the runner-up and print the output

l=[]
for i in range(0,5):
    ele = int(input("Enter numbers: "))
    l.append(ele)
    l.sort(reverse=True)
print(l[1])

#-------------------------------------------------------------------------------

#Q3
#WAP to read the record of n students in a dictionary containing key/value pairs of name: [marks].
#Print the average of the marks obtained by the particular student correct to 2 decimal places

record={}
n=int(input("enter the no. of records: "))
for i in range(0,n):
    name=str(input("\nEnter the name:"))
    mark1=int(input("Enter the marks of subject 1: "))
    mark2=int(input("Enter the marks of subject 2: "))
    mark3=int(input("Enter the marks of subject 3: "))
    record[name]=[int(mark1),int(mark2),int(mark3)]
name1=str(input("\nEnter the name of the student for average marks: "))
if name1 in record.keys():
      print("AVG:",sum(record[name1])/3)
