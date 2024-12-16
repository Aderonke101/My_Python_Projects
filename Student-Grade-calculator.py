def calculate_grade(scores):
    average_score = sum(scores) / len(scores)
    if 90 <= average_score <= 100: return 'A'
    elif 80 <= average_score < 90: return 'B'
    elif 70 <= average_score < 80: return 'C'
    elif 60 <= average_score < 70: return 'D'
    else:return 'F'
def main():print ("welcome to the Grade calculator Program!")
num_exams = int(input("How many exams or assignments do you want to enter scores for? "))
scores = []
for i in range(num_exams):
          score = float(input(f"please enter your score for Exam {i + 1}:"))
          scores.append(score)
          letter_grade = calculate_grade(scores)

          print("calculating your overall grade...")
          print(f"Your overall grade is: {letter_grade}")
          if __name__ == "__main__":main()

