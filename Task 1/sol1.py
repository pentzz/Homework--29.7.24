from func_without_return import *

#Task a
my_ascending(7, -12)

#Task b
my_details("AI is the best")

#Task c
say_bool(True)
say_bool(False)

#Task d
print_zugi([5, 3, 2, 10, 15, 14, 14])

#Task e
grades: list[int] = []
while True:
    grade: int = int(input("Please enter the grade: "))
    if grade == -99:
        break
    if grade < 0 or grade > 100:
        print("Please enter valid grade (0-100).")
        continue
    grades.append(grade)
my_statistics(grades)

#Task f
help(print_zugi)
help(my_statistics)
help(say_bool)
help(my_details)
help(my_ascending)