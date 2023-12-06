#Welcome message
print("Welcome to the tip calculator")

#Receiving total bill
total_bill = float(input("What was the total bill?\n$"))

#Receiving the tip
tip_percentage = int(input("What percentage tip would you like to give? 10, 12, or 15?\n"))

#Receiving how many people
number_people = int(input("How many people to split the bill?\n"))

#Calculations
split_bill = round((total_bill * (tip_percentage / 100 + 1)) / number_people, 2)

#Output
print(f"Each person should pay: ${split_bill}")