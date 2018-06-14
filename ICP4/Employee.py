class Emp:   # creating the class emp
    ec = 0     # initializing count to 0
    ts = 0      # initializing total salary to 0
    avgsal = 0

    def __init__(self, name, family, salary, department):   # defining a constructor  with the details we need
        self.name = name
        self.family = family
        self.salary = salary
        self.department = department
        Emp.ec += 1     # incrementing the count while adding data of each employee
        Emp.ts += int(salary)      # adding salary of employee wnen each employee salary is added

    def avg_sal(self):   # defining function to print the average salary
        print("average salary of %d" % (Emp.ts / Emp.ec))

    def inherit(self):
        print("This is  parent class")


class Fulltime_Employee(Emp):    # performing inheritace from the parent class(emp)
    def Extends(self):
        print("this is child class")


"""

    def displayCount(self):
        print("Total Employee %d" % Employee.empCount)
"""
emp1 = Emp("Ashish", "Motanam ", "11728", "CS")  # adding the details of each employee
emp2 = Emp("Ashu", "  Gurunadham", "21545", "CS")
emp3 = Emp("Supreme", "Motanam", "25451", "CS")
emp4 = Emp("Lokesh", "Ravichandra", "55151", "vet")
emp5 = Fulltime_Employee("Praneeth", "Patnam", "2462748", "CS")
print("Total Employee %d" % Emp.ec)
print("average salary %d" % (Emp.ts / Emp.ec))
# this is by function calling
emp4.avg_sal() # calling the function avg_sal
emp5.inherit()
emp5.Extends()