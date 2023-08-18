from employee import Employee

class Contractor(Employee):

    def __init__(self, name, id,  department, jobTitle, endDate, ABN, salary):
        super().__init__(name, id,  department, jobTitle)
        self.endDate = endDate
        self.ABN =  ABN
        self.salary =  salary

    def __str__(self):
        super(Contractor, self).toString()
        print("Contract End Date :", self.endDate, "ABN :", self.ABN, "Salary :", self.salary)
    