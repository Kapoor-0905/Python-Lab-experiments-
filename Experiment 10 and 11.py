#Q1
# Create a class Employee With following properties 
# *First Name, *Last Name, *Pay, *Email: Automatically generated as (First_Name+'.'+Last_Name+'@company.com')

class Employee:
    fname = input("Enter the first name: ")
    lname = input("Enter the last name: ")
    pay = int(input("Enter the pay: "))
    email = fname.lower()+'.'+lname.lower()+'@xyz.com'
    def employee(self):
        print("PROPERTIES:\n")
        print("First Name: ",self.fname)
        print("Last Name: ",self.lname)
        print("Pay: ",self.pay)
        print("Email ID: ",self.email)
x = Employee()
print(x.employee())

#---------------------------------------------------------------------------------------------------------------------

#Q2. Perform the following instructions:
# a) Create a Vehicle class with max_speed and mileage as instance attributes.
    #Additionally, create a method named seating_capacity() using the below syntax:
    #b) Create child class ‘Bus’ that will inherit all of the variables and methods of the Vehicle class. Set the seating capacity of the bus to 50 using super().
    #c) Create a Bus object that will inherit all of the variables and methods of the Vehicle class and display it.
    #d) Define a class attribute “color” with a default value white. I.e., Every Vehicle should be white.

class vehicle():
    def __init__(self,max_speed,mileage,name,color='white'):
        self.color = color
        self.name = name
        self.mileage = mileage
        self.max_speed = max_speed
    def seating_capacity(self,capacity):
        return f"The seating capacity of a {self.name} is {capacity} passengers"

class bus(vehicle):
    def __init__(self,max_speed,mileage,name,color):
        super().__init__(50)

bus = vehicle(100,50,'MAHINDRA')
bus.seating_capacity(10)
print(bus.max_speed)
print(bus.color)