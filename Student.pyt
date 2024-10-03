class Student:
    def __init__(self, first_name, last_name, age, reg_n0, course, level):
        self.fName = first_name
        self.lName = last_name
        self.age = age
        self.regN0 = reg_n0
        self.course = course
        self.year = level
    
    def __str__(self):
        print(f"""Hello {self.fName} {self.lName}
{self.course} is a nice course to pursue
it is fine to be in {self.year} if you have {self.age}
your registration number is {self.regN0}

        """)


joseph = Student('Joseph', 'Munyiko', 22, 'S23B13/115', 'Information Technology', 'Year 2')
one = joseph.__str__()
print(one)
benjamin = Student('Benjamin', 'Kingombe', 19, 'J23C00/045', 'Higher Education Certificate', 'Year 1')
two = benjamin.__str__()
print(two)