# UID: U72087839
# Name: Claude Watson
# Description: To quiz the user on state capitals and quit when a sentinel is entered.

import random

caps = {"Alabama": "Montgomery", "Alaska": "Juneau", "Arizona": "Phoenix", "Arkansas": "Little Rock", "California": "Sacramento",
        "Colorado": "Denver", "Connecticut": "Hartford", "Delaware": "Dover", "Florida": "Tallahassee", "Georgia": "Atlanta",
        "Hawaii": "Honolulu", "Idaho": "Boise", "Illinois": "Springfield", "Indiana": "Indianapolis", "Iowa": "Des Moines",
        "Kansas": "Topeka", "Kentucky": "Frankfort", "Louisiana": "Baton Rouge", "Maine": "Augusta", "Maryland": "Annapolis",
        "Massachusetts": "Boston", "Michigan": "Lansing", "Minnesota": "Saint Paul", "Mississippi": "Jackson",
        "Missouri": "Jefferson City", "Montana": "Helena", "Nebraska": "Lincoln", "Nevada": "Carson City", "New Hampshire": "Concord",
        "New Jersey": "Trenton", "New Mexico": "Santa Fe", "New York": "Albany", "North Carolina": "Raleigh",
        "North Dakota": "Bismarck", "Ohio": "Columbus", "Oklahoma": "Oklahoma City", "Oregon": "Salem", "Pennsylvania": "Harrisburg",
        "Rhode Island": "Providence", "South Carolina": "Columbia", "South Dakota": "Pierre", "Tennessee": "Nashville",
        "Texas": "Austin", "Utah": "Salt Lake City", "Vermont": "Montpelier", "Virginia": "Richmond", "Washington": "Olympia",
        "West Virginia": "Charleston", "Wisconsin": "Madison", "Wyoming": "Cheyenne"}


print("Press 'q' at anytime to quit.\n")  # sentinel
ans = ""
right = 0
wrong = 0


while ans != "q":

    prompt = random.choice(list(caps))  # random state generator
    ans = input(f"What is the capital of {prompt}: ")

    if ans == "q":
        continue
    elif ans == caps[prompt]:
        print("Correct.\n")
        right += 1
    elif ans != caps[prompt]:
        print("Wrong.\n")
        wrong += 1

print(f"You had {right} correct answers and {wrong} incorrect answers.")