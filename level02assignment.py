#Jenna Smedley
# Level 02 Assignment -- Road Trip Planner

#acquiring user info
user_name = input("Enter your name: ")
destination = input("Enter your destination: ")
one_way_distance = float(input("Enter your one-way distance in miles: "))
vehicle_mpg = float(input("Enter your vehicle's miles per gallon: "))
gas_ppg = float(input("Enter the gas price per gallon: "))
traveler_quantity = float(input("Enter your number of travelers: "))

#calculations
total_distance = (one_way_distance * 2)
gas_required = (total_distance / vehicle_mpg)
gas_cost = (gas_required * gas_ppg)
cost_per_traveler = (gas_cost / traveler_quantity)

#display summary
print(user_name.upper() + "'s trip to " + destination)
print(f"Total cost of trip: ${gas_cost:.2f}")
print(f"Cost per traveler: ${cost_per_traveler:.2f}")