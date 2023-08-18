from employee import Employee
from shiftEmployee import ShiftEmployee
from contractor import Contractor
import csv

employees = [
    Employee("Employee", 1,  "department1", "job1"),
    Employee("Name2", 2,  "deparatment2", "job2"),
    Employee("Name3", 3,  "department3", "job3"),
]
global id
id= 0
employeeMap = {

}

def init():
    try:
        with open('employee_file.csv', mode='r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            line_count = 0
            for row in csv_reader:
                if line_count == 0:
                    # print(f'Column names are {", ".join(row)}')
                    line_count += 1
                # print(f'\t{row["name"]} works in the {row["department"]} department, and was born in {row["birthday month"]}.')
                id = int(row["id"])
                employeeMap[id] = Employee(row["Name"], id, row["Department"], row["jobTitle"])

                line_count += 1
            csv_file.close()
    except IOError:
        print("No such file exist there")

def chageData():
    id = int(input("Please enter the ID for employee"))
    if id in employeeMap.keys():
        name = input("Please enter the Name for employee")
        Department = input("Please enter the Department for employee")
        job = input("Please enter the Job Titile for employee")
        employeeMap[id] = Employee(name, id, Department, job)
    else:
        print("Employee with the following ID  ",id,"doesn't not exists")
    
def addData():
    name = input("Please enter the Name for employee")
    Department = input("Please enter the department for employee")
    job = input("Please enter the job for employee")
    global id
    id +=1 
    employeeMap[id] = Employee(name, id, Department, job)

def deleteData():
    id = int(input("Enter the id:"))
    if id in employeeMap.keys():
        employeeMap.pop(id)
    else:
        print("Employee with",id,"doesn't not exists")

def closeProgram():
    with open('employee_file.csv', mode='w') as employee_file:
        employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        fieldnames = ['Name', 'id', 'Department', "jobTitle"]
        writer = csv.DictWriter(employee_file, fieldnames=fieldnames)

        writer.writeheader()
    
        for key in employeeMap:
            writer.writerow({"Name" : employeeMap[key].name, "id": employeeMap[key].id,  "Department": employeeMap[key].department, "jobTitle": employeeMap[key].jobTitle})

    employee_file.close()



print("---------------Creating three employees--------------------")
employees = [
    Employee("Susanna Myer", 47899, "Accounting", "Vice President"),
    Employee("Mark Joseph", 39119, "Info Tech", "Programmer"),
    Employee("Joyce Roberts", 81774, "Manufacturing" , "Engineer"),
]
print("---------------Printing three employees------------------")
for i in employees:
    i.toString()

print("-----------------Creating two ShiftEmployee--------------")
# (self, name, id,  department, jobTitle,  shiftNo, rate)
s1 = ShiftEmployee("Susanna Myer", 47899, "Accounting", "Vice President", 1 , 10)
s2 = ShiftEmployee("Mark Joseph", 30119, "Info Tech", "Programmer", 2 , 8)

print("-----------------Calling accessors--------------")
print("E1=>Name : ",s1.getName())
print("E2=>Job  : ",s2.getJob())


print("-----------------Calling Mutators--------------")
s1.setName(input("Enter the Name of Employee 1 to be changed :"))
s2.setJob(input("Enter the Job of Employee 2 to be changed :"))
print("E1=>Name : ",s1.getName())
print("E2=>Job  : ",s2.getJob())

print("------------creating two contractors-----------\n\n")
# (self, name, id,  department, jobTitle, endDate, ABN, salary)
c1 = Contractor("Susanna Myer", 47899, "Accounting", "Vice President", "1/2/2021" , 1242343274872, 10000)
c2 = Contractor("Mark Joseph", 30119, "Info Tech", "Programmer", "2/3/2021" , 213432895349, 8000)

print("---------------displaying their information----------------")
c1.__str__()
print()
c2.__str__()
print()
print("---------------Starting Main project-------------\n\n\n")


init()
while(True):
    print('''1. Look up an employee in the dictionary
        2. Add a new employee to the dictionary
        3. Change an existing employee’s name, department, and job title in the dictionary.
        4. Delete an employee from the dictionary
        5. Quit the program ''')
    ans =int( input("Enter the option"))
    if(ans == 1):
        for employee in employeeMap:
            employeeMap[employee].toString()
    elif(ans == 2):
        addData()
    
    elif(ans ==3 ):
        chageData()
    
    elif(ans == 4):
        deleteData()
    
    elif(ans == 5):
        closeProgram()
        exit()

    else:
        print("Invalid Option \n")
