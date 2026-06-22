# def write_lines(filename,lines):
#     with open(filename,"w")as file:
#         for line in lines:
#             file.write(line+"\n")
# name=["top","dok","east"]
# write_lines("app.txt",name)
# def count_lines(filename):
#     with open(filename,"r")as file:
#         return sum(1 for line in file)
# print(count_lines("app.txt"))

# with open("source.txt","r")as source:
#     with open("dest.txt","w")as dest:
#         for  line in source:
#             dest.write(line)
#
# import os
# if os.path.exists("data.txt"):
#     with open("data.txt","a")as file:
#         file.write("new entry")
# else:
#     with open("data.txt","w")as file:
#         file.write("new entry")
        
# import csv
# def read_csv_row(filename):
#     with open(filename, mode="r")as file:
#         reader=csv.reader(file)
#         next(reader)
#         return list(reader)
# print(read_csv_row("student.csv"))


# import csv
# def average_score(filename):
#     total=0
#     count=0
#     with open (filename,"r",newline="")as file:
#         reader=csv.DictReader(file)
#         for row in reader:
#             total+=float(row["Score"])
#             count+=1
#             return round(total/count,1)
# print(average_score("student.csv"))

# from datetime import datetime
# def append_log(message, logfile="apps.log"):
#     timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#     with open(logfile, "a") as file:
#         file.write(f"[{timestamp}] {message}\n")
# append_log("hello nikhil","apps.log")
# append_log("User logged in","apps.log")


# total=0
# with open("numbers.txt","r")as file:
#     for line in file:
#         line=line.strip()
#         if line:
#             total+=int(line)
# print(total)
# import csv
# def write_student_csv(filename,data):
#     with open(filename, mode="w", newline="")as file:
#         writer=csv.writer(file)
#         writer.writerows(data)
# student_data=[
#     ["Name","Age","Grade"],
#     ["top","22","9"],
#     ["dok","21","8"]
# ]
# import os

# def safe_read(filename):
#     if os.path.exists(filename):
#         with open(filename, "r") as file:
#             return file.read()
#     return "FILE NOT FOUND"
# print(safe_read("dest.txt"))


# import csv

# with open("students.csv", "r", newline="") as infile,\
#     open("top_students.csv", "w", newline="") as outfile:
#     reader = csv.DictReader(infile)
#     writer = csv.DictWriter(
#         outfile,
#         fieldnames=reader.fieldnames
#     )
#     writer.writeheader()
#     for row in reader:
#         if float(row["Score"]) >= 90:
#             writer.writerow(row)

# with open("sample.txt", "r") as file:
#     print(file.read())
# with open("sample.txt", "r") as file:
#     print(file.readline())
# with open("sample.txt", "r") as file:
#     print(file.readlines())


# def word_count(filename):
#     counts = {}
#     with open("samples.txt", "r") as file:
#         text = file.read().lower()
#     words = text.split()
#     for word in words:
#         counts[word] = counts.get(word, 0) + 1
#     return counts
# print(word_count("samples.txt"))


with open("samples.txt", "w+") as file:
    file.write("Line 1\n")
    file.write("Line 2\n")
    file.write("Line 3\n")
    file.seek(0)
    print(file.read())