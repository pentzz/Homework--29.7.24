from func import *

#Task e - Upgrade
grades: list[int] = []
while True:
    grade: int = get_int("Please enter a grade: ")
    if grade == -99:
        break
    if grade < 0 or grade > 100:
        print("Please enter valid grade (0-100).")
        continue
    grades.append(grade)
my_statistics(grades)