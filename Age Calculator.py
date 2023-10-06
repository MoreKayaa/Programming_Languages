#Favian Mokaya Imbera SCT211-0022/2021


#Input your date of birth in the format
#DD-MM-YYYY

from datetime import datetime

# Input
dob_input = input()

# Convert the input string to a datetime object
dob = datetime.strptime(dob_input, "%d-%m-%Y")

# Get the current date
current_date = datetime.now()

# Calculate the difference between the current date and the date of birth
age = current_date - dob

# Retrieve years, months, and days from the age difference
years = age.days // 365
remaining_days = age.days % 365
months = remaining_days // 30
days = remaining_days % 30

# Display the age in the format yyyy-mm-dd
formatted_age = current_date.strftime("%Y-%m-%d")
print(f"\n\nYou are {years} years, {months} months, and {days} days old.")
