# printing highest marks with subject name
def highestMarks(marksDict):
    maxMarks = 0
    subjectName = ""
    for subject, marks in marksDict.items():
        if (marks > maxMarks):
            maxMarks = marks
            subjectName = subject

    print(subjectName, maxMarks)


marks = {
    "physics": 80,
    "chemistry": 82,
    "maths": 90,
    "english": 89,
}
highestMarks(marks)
