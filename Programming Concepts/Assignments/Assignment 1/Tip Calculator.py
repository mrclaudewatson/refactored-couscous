# Name: CLaude Watson
# UID: U72087839
# Tip Calculator - To calculate the gratuity and print the total amount in dollars.

subtotal = float(input("What is the subtotal?:"))
gratuity = float(input("How much would you like to tip? (Enter your value as a percentage):")) / 100

gratuity = subtotal * gratuity
total = subtotal + gratuity

print("Your tip amount is ${:,.2f}".format(gratuity))
print("Your total amount is ${:,.2f}".format(total))