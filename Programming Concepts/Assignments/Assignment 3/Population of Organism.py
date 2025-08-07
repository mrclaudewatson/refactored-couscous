#UID: U72087839
#Name: Claude Watson
#Population of Organisms - To form a table displaying the number of days and population of an organism.

organisms = float(input("How many organisms are there?:"))
while organisms < 1:
    organisms = float(input("Invalid entry. How many organisms are there?:"))
avgpop_percent = float(input("What is the average daily increase as a percentage?:"))
while avgpop_percent < 1 or avgpop_percent > 100:
    avgpop_percent = float(input("Invalid entry. What is the average daily increase as a percentage?:"))
numdays = int(input("How long do the organisms have to multiply?:"))
while numdays < 1:
    numdays = int(input("Invalid entry. How long, in days, do the organisms have to multiply?:"))

print(f"\nDays\tPopulation\n------------------")

for i in range(1, numdays + 1):
    population = (avgpop_percent / 100 * organisms) + organisms
    if i == 1:
        population = organisms
    organisms = population
    print(f"{i}\t{population:6f}")


#PyCharm and IDLE display the table differently. I used IDLE to get a neat table.
