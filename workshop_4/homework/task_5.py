def letter_grade(score):
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'


def class_report(scores):
    for score in scores:
        print(f"Score: {score} -> Grade: {letter_grade(score)}")


scores = [77, 99, 15, 100, 91, 25]
class_report(scores)
print(sum(scores) / len(scores))