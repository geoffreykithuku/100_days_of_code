student_scores = {
    "Harry" : 81,
    "Ron" :78,
    "Hermione" :99,
    "Draco" :74,
    "Neville" : 62
}

grades = {}

for student in student_scores:
    score = student_scores[student]
    
    if score > 90:
        grades[student] = "Outstanding"
    elif score > 80:
        grades[student] = "Exceeds Expectations"
    elif score > 70:
        grades[student] = "Acceptable"
    else:
        grades[student] = "Failed"
        
print(grades)