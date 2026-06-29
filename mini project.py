import csv

students = []
next_id = 1


def calculate_grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 80:
        return "B"
    elif avg >= 70:
        return "C"
    elif avg >= 60:
        return "D"
    else:
        return "F"


def add_student():
    global next_id

    name = input("Enter Name: ")
    age = int(input("Enter Age: "))
    n = int(input("Enter Number of Subjects: "))

    scores = {}
    total = 0

    for i in range(n):
        subject = input("Enter Subject Name: ")

        while True:
            score = int(input("Enter Score: "))
            if 0 <= score <= 100:
                break
            print("Invalid Score! Enter between 0 and 100.")

        scores[subject] = score
        total += score

    average = total / n
    grade = calculate_grade(average)

    student = {
        "id": next_id,
        "name": name,
        "age": age,
        "scores": scores,
        "average": average,
        "grade": grade
    }

    students.append(student)
    next_id += 1

    print("Student Added Successfully!")


def view_students():
    if len(students) == 0:
        print("No records found.")
        return

    # Bubble Sort (Descending by Average)
    for i in range(len(students) - 1):
        for j in range(len(students) - i - 1):
            if students[j]["average"] < students[j + 1]["average"]:
                temp = students[j]
                students[j] = students[j + 1]
                students[j + 1] = temp

    print("\n-----------------------------------------------")
    print("ID\tName\tAge\tAverage\tGrade")
    print("-----------------------------------------------")

    for s in students:
        print(s["id"], "\t", s["name"], "\t", s["age"], "\t",
              round(s["average"], 2), "\t", s["grade"])


def search_student():
    if len(students) == 0:
        print("No records found.")
        return

    name = input("Enter Name to Search: ").lower()
    found = False

    for s in students:
        if name in s["name"].lower():
            print("\nID:", s["id"])
            print("Name:", s["name"])
            print("Age:", s["age"])
            print("Scores:", s["scores"])
            print("Average:", round(s["average"], 2))
            print("Grade:", s["grade"])
            found = True

    if found == False:
        print("Student Not Found.")


def delete_student():
    if len(students) == 0:
        print("No records found.")
        return

    sid = int(input("Enter Student ID: "))

    for s in students:
        if s["id"] == sid:
            students.remove(s)
            print("Student Deleted Successfully!")
            return

    print("Student ID Not Found.")


def update_student():
    sid = int(input("Enter Student ID: "))

    for s in students:
        if s["id"] == sid:

            n = int(input("Enter Number of Subjects: "))
            scores = {}
            total = 0

            for i in range(n):
                subject = input("Enter Subject Name: ")

                while True:
                    score = int(input("Enter Score: "))
                    if 0 <= score <= 100:
                        break
                    print("Invalid Score! Enter between 0 and 100.")

                scores[subject] = score
                total += score

            average = total / n
            grade = calculate_grade(average)

            s["scores"] = scores
            s["average"] = average
            s["grade"] = grade

            print("Student Record Updated!")
            return

    print("Student ID Not Found.")


def save_csv():
    file = open("students.csv", "w", newline="")
    writer = csv.writer(file)

    writer.writerow(["ID", "Name", "Age", "Scores", "Average", "Grade"])

    for s in students:
        writer.writerow([
            s["id"],
            s["name"],
            s["age"],
            str(s["scores"]),
            s["average"],
            s["grade"]
        ])

    file.close()
    print("Records Saved to students.csv")


def load_csv():
    try:
        file = open("students.csv", "r")
        reader = csv.reader(file)

        next(reader)

        print("\n-----------------------------------------------")
        print("ID\tName\tAge\tScores\tAverage\tGrade")
        print("-----------------------------------------------")

        for row in reader:
            print(row)

        file.close()

    except FileNotFoundError:
        print("CSV File Not Found.")


def class_statistics():
    if len(students) == 0:
        print("No records found.")
        return

    highest = students[0]
    lowest = students[0]

    total = 0

    grade_count = {
        "A": 0,
        "B": 0,
        "C": 0,
        "D": 0,
        "F": 0
    }

    for s in students:

        total += s["average"]

        if s["average"] > highest["average"]:
            highest = s

        if s["average"] < lowest["average"]:
            lowest = s

        grade_count[s["grade"]] += 1

    print("\nClass Statistics")
    print("----------------------------")
    print("Total Students:", len(students))
    print("Highest Average:", highest["name"], "-", round(highest["average"], 2))
    print("Lowest Average:", lowest["name"], "-", round(lowest["average"], 2))
    print("Class Average:", round(total / len(students), 2))
    print("Grade Counts:")
    print("A =", grade_count["A"])
    print("B =", grade_count["B"])
    print("C =", grade_count["C"])
    print("D =", grade_count["D"])
    print("F =", grade_count["F"])


while True:

    print("\n===== Student Record Management System =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Update Student Scores")
    print("6. Save to CSV")
    print("7. Load from CSV")
    print("8. Class Statistics")
    print("9. Exit")

    choice = input("Enter Your Choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        delete_student()

    elif choice == "5":
        update_student()

    elif choice == "6":
        save_csv()

    elif choice == "7":
        load_csv()

    elif choice == "8":
        class_statistics()

    elif choice == "9":
        print("Thank You!")
        break

    else:
        print("Invalid Choice!")