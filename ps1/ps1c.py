# Define the function for finding the best saving rate
def find_rate(starting_salary):
    # Parameters setup
    epsilon = 100  # Margin of error for target amount
    semi_annual_raise = .07  # Salary raise percentage every 6 months
    down_payment = 0.25  # Down payment is 25% of total cost
    total_cost = 1000000  # Total cost of house
    target = total_cost * down_payment  # Target amount needed for down payment
    monthly_salary = float(starting_salary) / 12  # Convert annual to monthly salary
    r = 0.04  # Annual return rate on investments
    steps = 0  # Counter for bisection search steps
    high = 10000  # Upper bound for savings rate (100%)
    low = 0  # Lower bound for savings rate (0%)
    
    # Check if reaching the down payment is possible within 3 years
    current_savings = 0
    temp_monthly_salary = monthly_salary
    for months in range(36):
        current_savings += current_savings * r / 12 + temp_monthly_salary
        if (months + 1) % 6 == 0:
            temp_monthly_salary = temp_monthly_salary * (1 + semi_annual_raise)
    if current_savings < target - epsilon:
        print("It is not possible to pay the down payment in three years.")
        return
    
    # Bisection search to find optimal savings rate
    while True:
        saving_rate = (high + low) / 2  # Calculate middle point
        current_savings = 0
        #months = 0
        temp_monthly_salary = monthly_salary
        
        # Simulate 36 months of savings with current rate
        #while months < 36:
        for months in range (36):
            current_savings += current_savings * r / 12 + temp_monthly_salary * saving_rate / 10000
            #months += 1
            if (months + 1) % 6 == 0:
                temp_monthly_salary = temp_monthly_salary * (1 + semi_annual_raise)
        
        # Adjust search range based on result
        if current_savings > target + epsilon:
            high = saving_rate  # We're saving too much, decrease rate
            steps += 1
        elif current_savings < target - epsilon:
            low = saving_rate  # We're saving too little, increase rate
            steps += 1
        else:
            # Found the optimal rate within acceptable error
            print("Best savings rate:", int(saving_rate) / 10000)
            print("Steps in bisection search:", steps)
            break
        
find_rate(float(input("Enter the starting salary: ")))