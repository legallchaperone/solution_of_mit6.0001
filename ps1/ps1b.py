# Get user input for annual salary, portion to save, and total cost of the dream home
annual_salary = float(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = float(input("Enter the cost of your dream home: "))
semi_annual_raise = float(input("Enter the semi-anual raise, as a decimal: "))

# Portion of the total cost needed for a down payment
portion_down_payment = 0.25

# Initial savings
current_savings = 0

# Annual return rate on savings
r = 0.04

# Calculate monthly salary
monthly_salary = float(annual_salary) / 12

# Initialize month counter
months = 0

# Loop until current savings reach the down payment amount
while current_savings < total_cost * portion_down_payment:
   # Add monthly savings and investment return to current savings
   current_savings += current_savings * r / 12 + monthly_salary * portion_saved
   # Increment month counter
   months = months + 1
   if months%6 == 0:
      monthly_salary = monthly_salary * (1 + semi_annual_raise)


# Output the number of months needed to save for the down payment
print("Number of months:", months)

# Notes on my learning process:
# 1. Learned to write a while loop with a clear condition, instead of using 'while True' with 'if ... break'.
# 2. Realized I need to update 'current_savings' each month, not just calculate its change.
# 3. Switched from using 'i' as a counter to the more descriptive 'months'.
