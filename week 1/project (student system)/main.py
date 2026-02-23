import models, analytics, utils

# std = models.Student()
# std.name = "Ammar"
# std.student_id = 1
# std.grades = [99,98,97]
# print(std.cat(std.average()))

cla = models.Classroom()
try:
    cla.add_student(4, "Ghalib", 79)
except Exception:
    print("Error")
cla.students += utils.import_students("data.csv")
# cla.find_student("Ali")
# cla.remove_student("Ali")
# cla.find_student("Ali")
print(cla.students)

print(models.Classroom.classroom_avg_list())
# print(cla.classroom_avg_list())

# print(analytics.top_student(cla.students))
# print(analytics.worst_student(cla.students))
# print(analytics.rank_student(cla.students))

# utils.export_students(cla.students)