# Exceptions

# exceptions - errors that can be reasonably handled
#try block - insert any code

# you can create your own expections via inheritance:
class RangeError(Exception):
    pass

try:
    value1 = int(input("Enter a numerator: "))
    value2 = int(input("Enter a denominator: "))

    ans = value1/value2

    #refer to pre-existing except blocks
except ValueError:
    print("Wrong value: integer expected.")

    #refer to mulitple exceptions in the same block
except(ValueError, TypeError):
    print('Value error or type error')

except ZeroDivisionError as message:
    print(message)

except:  # generic exception
    print("some other error has occured.")

else: #no exceptions encountered
    print(f"{value1}/{value2} = {ans}")


# another example
try:
    score = float(input("Enter score (0-100): "))
    if score < 0 or score > 100:
        raise RangeError
except RangeError:
    print("Invalid range.")

#optional finally block - code runs regardless of error or not (good for cleanup)
finally:
    print("Done with this code.")