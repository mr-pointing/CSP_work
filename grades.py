# Richard Pointing
# Activity 1.1.8
my_courses = ["English", "Math", "CS"]

done = False

while not done:
    grades = []
    for course in my_courses:
        c_grade = int(input("Enter your grade number: "))
        if c_grade >= 90:
            print("Grade: A")
            grades.append("A")
        elif 90 > c_grade >= 80:
            print("Grade: B")
            grades.append("B")
        elif 80 > c_grade >= 70:
            print("Grade: C")
            grades.append("C")
        elif 70 > c_grade >= 65:
            print("Grade: D")
            grades.append("D")
        else:
            print("Failed")
            grades.append("F")
    for course, grade in zip(my_courses, grades):
        print(f"{course}: {grade}")
    retry = input("Enter to restart, or DONE to end")
    if retry == "DONE":
        done = True
