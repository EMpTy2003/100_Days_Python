#High Score
#program to calculate the highest score from a list of scores

student_scores=input("Scores: ").split()
for n in range(0, len(student_scores)):
    student_scores[n]= int(student_scores[n])
print(student_scores) 

highscore=0
for score in student_scores:
    if score > highscore:
        highscore=score
print(f"Highest score is {highscore}")