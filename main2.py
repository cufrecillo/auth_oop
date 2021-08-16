class Employee:
    salary_raise = 1.04

    def __init__(self, name, last, salary):
        self.name = name
        self.last = last
        self.salary = salary
    
    def __str__(self):
        return f"Name: {self.name} -- Last: {self.last}\nSalary: {self.salary}"
    
    def apply_raise(self):
        self.salary *= self.salary_raise
    
    @classmethod
    def set_salary_raise(cls, value):
        cls.salary_raise = value

class Developer(Employee):
    salary_raise = 1.10
    
    def __init__(self, name, last, salary, p_language):
        super().__init__(name, last, salary)
        self.p_language = p_language
    
    def __str__(self):
        return f"Name: {self.name} -- Last: {self.last}\nSalary: {self.salary}\nP_Language: {self.p_language}"


user_employee = Employee("Bud", "Spencer", 10000)
user_developer = Developer("Peter", "Griffin", 12500, "Python")
print(user_employee)
user_employee.apply_raise()
print(user_employee.salary)
user_employee.apply_raise()
print(user_employee.salary)
user_employee.apply_raise()
print(user_employee.salary)
print(user_developer)
user_developer.apply_raise()
print(user_developer.salary)
user_developer.apply_raise()
print(user_developer.salary)
user_developer.apply_raise()
print(user_developer.salary)