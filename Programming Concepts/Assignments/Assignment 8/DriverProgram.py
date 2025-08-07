# UID: U72087839
# Name: Claude Watson
# Description: Executes the trivia game based off the trivia questions.

from TriviaQuestions import TriviaQuestions

turn = 0
p1_score = 0
p2_score = 0

question = TriviaQuestions()  # sets object

for i in question:

    if turn == 0:
        print("Question for Player 1: ")
    else:
        print("Question for Player 2: ")

    print(i)  # prints questions and possible answers1
    ans = int(input("Select a choice: "))
    while ans < 1 or ans > 4:
        ans = int(input("Select a choice: "))

    if ans == i.correct_ans and turn == 0:
        print("Correct!\n")
        p1_score += 1
    elif ans == i.correct_ans and turn == 1:
        print("Correct!\n")
        p2_score += 1
    else:
        print(f"Incorrect. The correct answer is {i.correct_ans}.\n")

    if turn == 0:
        turn += 1
    else:
        turn -= 1

print(f"Player 1 has {p1_score} points and Player 2 has {p2_score} points.")
if p1_score > p2_score:
    print("Player 1 won!")
elif p1_score == p2_score:
    print("Its a tie!")
else:
    print("Player 2 won!")
