score = input('Enter your grade score, between 0.0 and 1.0 \n')
try:
    score = float(score)
    if score > 1 or score < 0:
        print("Enter a score between 0 and 1")
    else:
        if score >= 0.9:
            grade = "A"
        elif score >= 0.8:
            grade = "B"
        elif score >= 0.7:
            grade = "C"
        elif score >= 0.6:
            grade = "D"
        else:
            grade = "F"
        print(grade)
except:
    print("include only alpha-numeric characters")