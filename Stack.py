#Python Data Structures: Stacks - Undo/Redo program built using a stack

class Employee:

    def __init__(self, first_name, last_name, middle_initial, age, department):
        self.first_name = first_name
        self.last_name = last_name
        self.middle_initial = middle_initial
        self.age = age
        self.department = department

    def getName(self):
        return self.first_name + " " + self.last_name

    def getAge(self):
        return self.age

    def getDepartment(self):
        return self.department


class Stack:

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        return self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)


class Functions:

    def __init__(self):
        self.employeeStack = Stack()
        self.history = Stack()

    def undo(self):
        employee = self.employeeStack.pop()
        self.history.push(employee)
        return "Undo Completed: Employee - " + employee.getName() + " has been removed"
    
    def redo(self):
        employee = self.history.pop()
        self.employeeStack.push(employee)
        return "Redo Completed: Employee - " + employee.getName() + " has been re-added"

    def addEmployee(self, first_name, last_name, middle_initial, age, department):
        emp = Employee(first_name, last_name, middle_initial, age, department)
        self.employeeStack.push(emp)
        return "Employee " + emp.getName() + " Has been added"
    


