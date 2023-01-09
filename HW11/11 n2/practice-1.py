import sys
sum_grade = 0
for grade in sys.argv[1:]:
    sum_grade += float(grade)
print(f"Average = {sum_grade/(len(sys.argv[1:]))}")

