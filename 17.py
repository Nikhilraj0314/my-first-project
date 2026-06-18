employee={
    101:{"name":"Tap","department":"cse","salary":30000},
    102:{"name":"Dok","department":"ece","salary":60000},
    103:{"name":"Top","department":"ee","salary":100000}
}
highest_salary={}
highest_employee={}
for emp_id,info in employee.items():
    dept=info["department"]
    salary=info["salary"]
    name=info["name"]
    
    if dept not in highest_salary:
        highest_salary[dept]=salary
        highest_employee[dept]=name
    
        
    elif salary>highest_salary[dept]:
        highest_salary[dept]=salary
        highest_employee[dept]=name
    print(highest_salary)
for dept in highest_salary:
    print(f"(salary:{highest_salary[dept]})  {dept}:{highest_employee[dept]}")