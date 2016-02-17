# Number of cars
cars = 100
# Capacity of each car
space_in_a_car = 4.0
# Number of drivers
drivers = 30
# Number of passengers
passengers = 90
# Number of cars that are not driven which is the number of cars minus number of drivers.  Crude
cars_not_driven = cars - drivers
# Cars driven is just the number of drivers.  Again crude
cars_driven = drivers
# Carpool capacity is the number of cars driven times the capacity of the car.
carpool_capacity = cars_driven * space_in_a_car
# average passengers per car is the number of passengers divided by the number of cars driven.
average_passengers_per_car = passengers / cars_driven


print "There are ", cars, "cars available."
print "There are only", drivers, "drivers available"
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."
print "Hey %s there." % "you"
