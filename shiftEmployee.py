from employee import Employee

class ShiftEmployee(Employee):

    def __init__(self, name, id,  department, jobTitle,  shiftNo, rate):
        super().__init__(name, id,  department, jobTitle)
        self.shiftNo = shiftNo
        self.rate =  rate

    def __str__(self):
        super(ShiftEmployee, self).toString()
    
    
    def getShiftNo(self):
        return self.shiftNo

    def getRate(self):
        return self.rate

    def setShiftNo(self, shiftNo):
        self.shiftNo = shiftNo

    def setRate(self, rate):
        self.rate = rate
