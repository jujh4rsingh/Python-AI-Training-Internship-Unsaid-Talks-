def input_student_data():
    students = {}
    subjects = input("Enter the subject names (comma-separated): ").split(',')

    n = int(input("Enter the number of students: "))
    for _ in range(n):
        name = input("\nEnter student name: ")
        scores = {}
        for subject in subjects:
            score = int(input(f"Enter marks in {subject.strip()}: "))
            scores[subject.strip()] = score
        students[name] = scores
    return students, subjects

def calculate_averages_and_grades(students, subjects):
    results = {}
    for name, scores in students.items():
        total = sum(scores.values())
        avg = total / len(subjects)
        grade = assign_grade(avg)
        results[name] = {'average': avg, 'grade': grade}
    return results

def assign_grade(avg):
    if avg >= 90:
        return 'A+'
    elif avg >= 80:
        return 'A'
    elif avg >= 70:
        return 'B'
    elif avg >= 60:
        return 'C'
    elif avg >= 50:
        return 'D'
    else:
        return 'F'

def find_subject_toppers(students, subjects):
    toppers = {}
    for subject in subjects:
        max_score = max([scores[subject] for scores in students.values()])
        toppers[subject] = [name for name, scores in students.items() if scores[subject] == max_score]
    return toppers

def highlight_patterns(toppers):
    same_top_scorers = set()
    for subject, names in toppers.items():
        if len(names) > 1:
            same_top_scorers.add((subject, tuple(names)))
    return same_top_scorers

def print_report(students, results, toppers, patterns):
    print("\n--- Student Report Card ---")
    for name, data in results.items():
        print(f"{name}: Average = {data['average']:.2f}, Grade = {data['grade']}")

    print("\n--- Subject-wise Toppers ---")
    for subject, names in toppers.items():
        print(f"{subject}: {', '.join(names)}")

    if patterns:
        print("\n--- Interesting Patterns (Same Top Scorers) ---")
        for subject, names in patterns:
            print(f"{subject}: Top scorers - {', '.join(names)}")

# Main Execution
students, subjects = input_student_data()
results = calculate_averages_and_grades(students, subjects)
toppers = find_subject_toppers(students, subjects)
patterns = highlight_patterns(toppers)
print_report(students, results, toppers, patterns)
