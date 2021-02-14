class Employee:
    def __init__(self,_name, **kwargs):
        a = _name.split(" ")
        self.name = a[0]
        self.lastname = a[1]
        self.salary = kwargs.get('salary', None)
        self.height = kwargs.get('height', None)
        self.nationality = kwargs.get('nationality', None)

john = Employee("John Doe")
mary = Employee("Mary Major", salary=120000)
richard = Employee("Richard Roe", salary=110000, height=178)
giancarlo = Employee("Giancarlo Rossi", salary=115000, height=182, nationality="Italian")

print(john.name)
print(mary.lastname)
print(richard.height)
print(giancarlo.nationality)