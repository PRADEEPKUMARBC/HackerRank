n = int(input().strip())

students = []
for i in range(n):
    name = input().strip()
    score = float(input().strip())
    students.append([name, score])
    
grades = [s[1] for s in students]
unique_sorted_grades = sorted(set(grades))
    
second_lowest = unique_sorted_grades[1]
names_with_second_lowest = sorted([s[0] for s in students if s[1] ==second_lowest])

for name in names_with_second_lowest:
    print(name)
    