class Class:
    __students_count = 22

    def __init__(self, name) -> None:
        self.name = name
        self.students = []
        self.grades= []

    def add_student(self, name, grade):
        if len(self.students) < Class.__students_count:
            self.students.append(name)
            self.grades.append(grade)
    
    def get_average_grade(self):
        avg = sum(self.grades) / len(self.grades)
        return float(f"{avg:.2f}")

    def __repr__(self) -> str:
        return f"The students in {self.name}: {', '.join(self.students)}. Average grade: {self.get_average_grade()}"

b_class = Class("11B")
b_class.add_student("Peter", 4.80)
b_class.add_student("George", 6.00)
b_class.add_student("Amy", 3.50)
print(b_class)

a_class = Class("11A")
a_class.add_student("Gosho", 3.30)
a_class.add_student("Ivan", 4.50)
a_class.add_student("Mimi", 6.00)
print(a_class)
