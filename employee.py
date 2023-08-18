class Employee:
    
    def __init__(self, name, id,  department, jobTitle):
        self.name = name
        self.id = id
        self.department = department
        self.jobTitle = jobTitle

    def toString(self):
        print("Name", self.name, ", ID:", self.id,  ", Dept:", self.department, ", Job Title", self.jobTitle)
        
    def getName(self):
        return self.name

    def getId(self):
        return self.id

    def getDepartment(self):
        return self.department

    def getJob(self):
        return self.jobTitle

    def setName(self, name):
        self.name = name

    def setId(self, id):
        self.id = id

    def setDepartment(self, department):
        self.department = department

    def setJob(self, jobTitle):
        self.jobTitle = jobTitle
