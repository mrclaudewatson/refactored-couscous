# UID: U72087839
# Name: Claude Watson
# Description: Creation of a function at creates a list of trivia questions.

import QuestionsClass

def TriviaQuestions():
    qlist = []

    qlist.append(QuestionsClass.Questions("How many days are in a lunar year?", "1. 354", "2. 365", "3. 243", "4. 379",
                                          1))

    qlist.append(QuestionsClass.Questions("What is the largest planet?", "1. Mars", "2. Jupiter", "3. Earth", "4. Pluto"
                                          , 2))

    qlist.append(QuestionsClass.Questions("What is the largest kind of whale?", "1. Orca Whale", "2. Humpback Whale",
                                          "3. Beluga Whale", "4. Blue whale", 4))

    qlist.append(QuestionsClass.Questions("Which dinosaur could fly?", "1. Triceratops", "2. Tyrannosaurus Rex",
                                          "3. Pteranodon", "4. Diplodocus", 3))

    qlist.append(QuestionsClass.Questions("Which of these Winnie the Pooh character is a donkey?", "1. Pooh",
                                          "2. Eeyore", "3. Piglet", "4. Kanga", 2))

    qlist.append(QuestionsClass.Questions("What is the hottest planet?", "1. Mars", "2. Pluto", "3. Earth", "4. Venus",
                                          4))

    qlist.append(QuestionsClass.Questions("Which dinosaur had the largest brain compared to body size?", "1. Troodon",
                                          "2. Stegosaurus", "3. Ichthyosaurus", "4. Gigantoraptor", 1))

    qlist.append(QuestionsClass.Questions("What is the largest type of penguin?", "1. Chinstrap",
                                          "2. Maracaroni Penguins", "3. Emperor Penguins", "4. White-flippered penguin",
                                          3))

    qlist.append(QuestionsClass.Questions("Which children's strpy character is a monkey?", "1. Winnie the Pooh",
                                          "2. Curious George", "3. Horton", "4. Goofy", 2))

    qlist.append(QuestionsClass.Questions("How long is a year on Mars?", "1. 550 Earth days", "2. 498 Earth days",
                                          "3. 126 Earth days", "4. 687 Earth days", 4))

    return qlist
