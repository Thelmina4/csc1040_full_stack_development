# ex1python.py

subject = "Computer Science"
year = 2
is_enrolled = True
if is_enrolled:
    print(f"{subject} - Year {year}")
else:
    print("Not enrolled")

marks = [62, 45, 78, 91, 55, 83]
total = 0
for mark in marks:
    total += mark
average = total / len(marks)
print(f"Average Mark: {average}")

for mark in marks:
    if mark >= 40:
        print(f"{mark} - Pass")
    else:
        print(f"{mark} - Fail")