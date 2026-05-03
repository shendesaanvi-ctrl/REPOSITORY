class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Employee(Person):
    def __init__(self, name, age, emp_id):
        super().__init__(name, age)
        self.emp_id = emp_id

class Manager(Employee):
    def __init__(self, name, age, emp_id, dept):
        super().__init__(name, age, emp_id)
        self.dept = dept

    def display(self):
        print(self.name, self.age, self.emp_id, self.dept)

# Example
m = Manager("Saanvi", 20, 101, "IT")
m.display()
