class Person(object):
    def __init__(self, name, age, education):
        self.name = name
        self.age = age
        self.education = education

    def work(self):
        print("%s goes to work" % self.name)


class Employee(Person):
    def __init__(self, name, age, education, salary):
        super(Employee, self).__init__(name, age, education)
        self.salary = salary

    def earn(self):
        print("%s got their paycheck" % self.name)


class Programmer(Employee):
    def __init__(self, name, age, education, salary):
        super(Programmer, self).__init__(name, age, education, salary)

    def code(self):
        print("%s coded some code on a computer" % self.name)


programmer1 = Programmer('Jonah', '25', 'Harvard University', 'Jonah earns 1,500')
programmer1.code()