# Makes "cars" equal to "100"
cars																	= 100
# Makes "space_in_a_car" equal to "4.0"
space_in_a_car 															= 4.0
# Makes "drivers" equal to "30"	
drivers																	= 30
# Makes "passengers" equal to "90"
passengers 																= 90
# Calculates cars not driven by: cars - drivers
cars_not_driven															= cars - drivers
# Makes "cars_driven" equal to "drivers"
cars_driven 															= drivers
# Calculates carpool capacity by: cars_driven * space_in_a_car
carpool_capacity 														= cars_driven * space_in_a_car
# Calculates average passengers per car by: passengers / cars_driven
average_passengers_per_car												= passengers / cars_driven

print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."

