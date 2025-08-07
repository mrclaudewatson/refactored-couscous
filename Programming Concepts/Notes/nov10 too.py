#Inheritance
#driver program

import vech
#Create a Vehicle object
ve1 = vech.Vehicle('Hyundai', 'Elantra', 2019)
print(f'I drive a {ve1.getyear()} {ve1.getmake()} {ve1.getmodel()}.')
#Create a Car object
car1 = vech.Car('Honda', 'Accord', 2021, 4)
print(f'My neighbor drives a {car1.getyear()} {car1.getmake()} \
{car1.getmodel()} with {car1.getdoors()} doors.')
#create an Electric Car object
ecar1 = vech.ElectricCar('Chevy', 'Volt', 2022, 4, 75)
print(f'My friend drives a {ecar1.getyear()} {ecar1.getmake()} \
{ecar1.getmodel()} with {ecar1.getdoors()} doors.')
print(f'Their car has a battery voltage of {ecar1.getbatvolt()} volts.')