# UID: U72087839
# Name: Claude Watson
# Description: Creation of a class that has attributes: trivia question, answer 1, 2, 3 & 4 and the number of the
#              correct answer

class Questions:
    def __init__(self, q, a1, a2, a3, a4, ca):
        self.__trivia_question = q
        self.__answer1 = a1
        self.__answer2 = a2
        self.__answer3 = a3
        self.__answer4 = a4
        self.correct_ans = ca  # Unhidden bc I will use it later to check the answer

    def __str__(self):
        return f"{self.__trivia_question}\n{self.__answer1}\n{self.__answer2}\n{self.__answer3}\n{self.__answer4}"
