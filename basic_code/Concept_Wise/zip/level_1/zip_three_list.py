subjects = ['Maths', 'DSA', 'DBMS', "Networking", "Operating system"]
marks = [9,8,7,9,10]
grades = ['A', 'B', 'c', 'A', 'AA']

for subject, mark, grade in zip(subjects, marks, grades):
    print(f"{subject}: {mark} {grade}")