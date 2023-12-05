# This Script reads a CSV resourse file for PYBank project.
# The financial dataset is called buget_data.csv
# The dataset is composed of two columns:  "Date" and "profit/losses"

# Task: Python script that analyzes the records to calculate each of the following values:
#	The total number of months included in the dataset
#	The net total amount of "Profit/Losses" over the entire period
#	The changes in "Profit/Losses" over the entire period, and then the average of those changes
#	The greatest increase in profits (date and amount) over the entire period
#	The greatest decrease in profits (date and amount) over the entire period

# Utilize Built-in Modules for Python to navigate across our file system:
#	Import os - lets Python know our operating system is Windows

#	Import csv - module for importing csv files

# back up one directory and then forward one directory to read csv file


import os
import csv

# Navigate to the correct directory
current_directory = os.getcwd()
csv_file_path = os.path.join(current_directory, '..', 'resources', 'budget_data.csv')

# Initialize variables
total_months = 0
total_profit_loss = 0
previous_profit_loss = None
monthly_change = []
months = []

# Read the CSV file
with open(csv_file_path, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    header = next(csvreader)

    for row in csvreader:
        # Count the total number of months
        total_months += 1

        # Sum up the total "Profit/Losses"
        total_profit_loss += int(row[1])

        # Calculate the monthly change in "Profit/Losses"
        if previous_profit_loss is not None:
            change = int(row[1]) - previous_profit_loss
            monthly_change.append(change)
            months.append(row[0])

        previous_profit_loss = int(row[1])

# Calculate the average change, greatest increase and decrease in profits
average_change = round(sum(monthly_change) / len(monthly_change), 2) if monthly_change else 0
greatest_increase = max(monthly_change) if monthly_change else 0
greatest_decrease = min(monthly_change) if monthly_change else 0
greatest_increase_month = months[monthly_change.index(greatest_increase)] if monthly_change else 'N/A'
greatest_decrease_month = months[monthly_change.index(greatest_decrease)] if monthly_change else 'N/A'

# Create the analysis text
analysis_text = (
    "Financial Analysis\n"
    "-------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${total_profit_loss}\n"
    f"Average Change: ${average_change}\n"
    f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})\n"
    f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})\n"
)

# Print the analysis to the terminal
print(analysis_text)

# Write the analysis to a text file
output_file_path = os.path.join(current_directory, 'Financial_Analysis.txt')
with open(output_file_path, 'w') as textfile:
    textfile.write(analysis_text)
