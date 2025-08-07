# Name: CLaude Watson
# UID: U72087839
# Runway Length - To input two values and calculate the minimum runway length needed for an airplane's takeoff.

v = float(input("Enter a speed in m/s. (Do not include units):"))
a = float(input("Enter an acceleration in m/s^2. (Do not include units):"))
runway_length = (v**2) / (2 * a)
print("The minimum length for the runway is {:,.4f} meters.".format(runway_length))