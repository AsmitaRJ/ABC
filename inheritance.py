class Person:
    def set_data(self, org, code):
        self.org = org
        self.code = code

class Department(Person):
    def get_data(self,dept,id):
        self.dept = dept
        self.id = id

class Student(Department):
    def set_name(self,name,sub):
        self.name = name
        self.sub = sub

    def display(self):
        print(f'Organization: {self.org} \nCode: {self.code} \nDepartment: {self.dept} \nID: {self.id} \nName: {self.name} \nSubject: {self.sub}')

obj = Student()
obj.set_data("MIT ADT University","0012")
obj.get_data("Bioengineering","12")
obj.set_name("Asmita Jagadale", "System Biology")
obj.display()