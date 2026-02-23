import csv

def import_students(stud_file: str):
    with open(stud_file, 'r') as file:
        students = csv.reader(file)
        students = list(students)
    return students


def export_students(stud_data: list):
    with open("exported_data.csv", 'w') as file:
        writer = csv.writer(file)
        for x in range(len(stud_data)):
            writer.writerow([stud_data[x][0], stud_data[x][1], stud_data[x][2]])

