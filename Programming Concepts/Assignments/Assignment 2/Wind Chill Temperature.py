#Name: Claude Watson
#UID: U72087839
# Wind Chill Temperature - To calculate and display the wind chill temperature, provided a temperature in fahrenheit.

temp = float(input("Enter a temperature between -58 degrees Fahrenheit and 41 degrees Fahrenheit. (Do not include units):"))
while temp not in range( -58, 41):
    print("Try again! This time, follow the instructions.")
    temp = float(input("Re-enter a temperature between -58 and 41 degrees Fahrenheit:"))


wind_speed = float(input("Enter a wind speed in mph. (Do not include units):"))
while wind_speed < 2:
    print("Try again! This time, follow the instructions.")
    wind_speed = float(input("Re-enter a wind speed in mph:"))

wind_chill_temp = 35.74 + 0.6215 * temp - 35.75 * wind_speed ** 0.16 + 0.4275 * temp * (wind_speed) ** 0.16

print("The wind chill is", wind_chill_temp.__round__(2))