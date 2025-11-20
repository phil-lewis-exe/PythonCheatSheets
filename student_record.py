class StudentRecord:
    def __init__(self, name, student_num, degree):
        self.name = name
        self.student_num = student_num
        self.degree = degree
        self.grade_dict = {}
        return
    
    def __str__(self):
        mystr = "*"*30+"\n"
        mystr += self.name+"\n"
        mystr += f"Student Number: {self.student_num}\n"
        mystr += f"Degree: {self.degree}\n"
        mystr += "Modules & Grades:\n"
        for key in self.grade_dict.keys():
            module = key
            grade = self.grade_dict[key]
            mystr += f"  {module}: {grade} \n"
        mystr += f"Average Grade: {self.calculate_grade_average()}\n"
        mystr += "*"*30
        return mystr

    def enter_grade(self, module_code, grade):
        self.grade_dict[module_code] = grade

    def calculate_grade_average(self):
        total = 0
        keys = self.grade_dict.keys()
        n = len(keys)
        for key in keys:
            total +=  self.grade_dict[key]
        av_grade = total/n
        return av_grade

    
