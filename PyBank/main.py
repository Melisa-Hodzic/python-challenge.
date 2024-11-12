# -*- coding: UTF-8 -*-
"""PyBank Homework Starter File."""

# Dependencies
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "budget_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "budget_analysis.txt")  # Output file path

# Define variables to track the financial data
total_months = 0
total_net = 0

# Add more variables to track other necessary financial data
total_changes = 0
average_change = 0
greatest_decrease = ["", 9999999]
greatest_increase = ["", 0]

# Initialize lists to store months and profits/losses
months = []
profit_losses = []
changes = []

# Open and read the csv
with open(file_to_load) as financial_data:
    reader = csv.reader(financial_data)

    # Skip the header row
    header = next(reader)

    # Extract first row to avoid appending to net_change_list
    first_row = next(reader)
    months.append(first_row[0])
    profit_losses.append(int(first_row[1]))
    total_months += 1
    total_net += profit_losses[0]

    # Set previous_profit for the first iteration
    previous_profit = profit_losses[0]

    # Process each row of data
    for row in reader:
        months.append(row[0])
        current_profit = int(row[1])
        profit_losses.append(current_profit)
        total_months += 1
        total_net += current_profit

        # Track the total/ monthly change
        monthly_change = current_profit - previous_profit
        changes.append(monthly_change)
        total_changes += monthly_change
        previous_profit = current_profit

        # Calculate the greatest increase in profits (month and amount)
        if monthly_change > greatest_increase[1]:
            greatest_increase[0] = row[0]
            greatest_increase[1] = monthly_change

        # Calculate the greatest decrease in losses (month and amount)
        if monthly_change < greatest_decrease[1]:
            greatest_decrease[0] = row[0]
            greatest_decrease[1] = monthly_change

# Calculate the average net change across the months
average_change = total_changes / len(changes) if changes else 0

# Generate the output summary
output = (
    "Financial Analysis\n"
    "-----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${total_net}\n"
    f"Average Change: ${average_change:.2f}\n"
    f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n"
    f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n"
)

# Print the output
print(output)

# Write the results to a text file
with open(file_to_output, "w") as txt_file:
    txt_file.write(output)

