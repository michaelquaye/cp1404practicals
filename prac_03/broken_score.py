"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

# TODO: Fix this!

def main():
    score = float(input("Enter score: "))
    result = evaluate_score(score)

    print(result)

def evaluate_score(score):
    if score < 0 or score > 100:
        print("Invalid score")
        result = "Invalid score"
    elif score >= 90:
        print("Excellent")
        result = "Excellent"
    elif score >= 50:
        print("Passable")
        result = "Passable"
    else:
        print("Bad")
        result = "Bad"
    return result
main()
