class Student:
    student_id = ""
    name = ""
    grades = []

    def average(self):
        sum_grades = 0
        for x in range(len(self.grades)):
            sum_grades += self.grades[x]
        
        # print(f"sum_grades = {sum_grades}")
        # print(f"len(self.grades) = {len(self.grades)}")
        print(sum_grades / len(self.grades))

        return (sum_grades / len(self.grades))
    
    
    def cat(self, avg):
        if 90 <= avg <= 100:
            return "Great"
        elif 80 <= avg < 90:
            return "Very Good"
        elif 70 <= avg < 80:
            return "Good"
        elif 60 <= avg < 70:
            return "Acceptable"
        else:
            return "Bad"
    

class Classroom:

    students = []

    def add_student(self, student_id: int, name: str, grades: list):
        stud_temp = []
        stud_temp.append(student_id)
        stud_temp.append(name.capitalize())
        stud_temp.append(grades)

        self.students.append(stud_temp)
    

    def remove_student(self, name):
        found_sublist = next((subl for subl in self.students if name in subl), None)
        self.students.remove(found_sublist)
    
    
    def find_student(self, name: str):
        if name.capitalize() in self.students:
            print("The Student does Exist")
        else:
            print("The Student does not Exist")

    @classmethod
    def classroom_avg_list(self):
        classromm_sum = 0
        for x in range(len(self.students)):
            classromm_sum += int(self.students[x][2])
        
        return f"Classroom Avg = {(classromm_sum // len(self.students))}"
