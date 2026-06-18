students=[
    {"name":"jack","age":"22","grade":[99,85]},
    {"name":"bob","age":"22","grade":[59,85]},
    {"name":"job","age":"22","grade":[55,85]}                                        
]
best_student = students[1]
best_average = sum(best_student["grade"]) / len(best_student["grade"])
min_age = best_student["age"]
for student in students:
    grade = student["grade"]
    avg=sum(grade)/len(grade)
    current_age =student["age"]
    if avg > best_average:
        best_average=avg
        best_student=student
    elif avg == best_average:
        if current_age < min_age:
            min_age=current_age
        best_student = student
print(best_student)
print(avg)