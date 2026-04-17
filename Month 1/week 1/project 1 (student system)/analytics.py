
def worst_student(students):
    sorted_student = sorted(students, key=lambda key:key[1])
    return f"The Wrost Student: {sorted_student[0]}"
    # print( sorted_student )

def top_student(students):
    sorted_student_revers = sorted(students, key=lambda key:key[1], reverse=True)
    return f"The Top Student: {sorted_student_revers[0]}"

def rank_student(students):
    sorted_student_revers = sorted(students, key=lambda key:key[1], reverse=True)
    return f"Students Rank: {sorted_student_revers}"


