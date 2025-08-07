# Name: CLaude Watson
# UID: U72087839
# Ingredient Adjuster - To calculate and display the adjusted amount of each ingredient for the specified number of cookies.

numcookies = int(input("How many cookies would you like to bake?:"))

COOKIES = 48
SUGAR = 1.5
BUTTER = 1
FLOUR = 2.75

sugar = (numcookies * SUGAR) / COOKIES
butter = (numcookies * BUTTER) / COOKIES
flour = (numcookies * FLOUR) / COOKIES

print(f"To make {numcookies} delicious cookies, you will need:")
print("{:,.2f} cups of sugar".format(sugar))
print("{:,.2f} cups of butter".format(butter))
print("{:,.2f} cups of flour".format(flour))
print("Happy baking!")