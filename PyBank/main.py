import os
import csv
import statistics

# Set CSV path for reading
csvpath = os.path.join('Resources','budget_data.csv')

# Set path to output .txt file
output_path = os.path.join('Analysis','financial_analysis.txt')

# Initialize lists to store Date and Profit/Loss info
date = []
profit = []
change = []
printlines = []

# Read CSV
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    # Skip header
    next(csvreader)

    # Adds Dates and Profits to respective arrays
    for row in csvreader:
        date.append(row[0])
        profit.append(row[1])

    # Changes Profits to integers rather than strings
    for i in range(0, len(profit)):
        profit[i] = int(profit[i])

    # Finds and stores the month-to-month profits
    for i in range(0, len(profit)-1):
        change.append(profit[i+1] - profit[i])
    
    # Finds the index of the maximum and minimum profit
    max_index = profit.index(max(profit))
    min_index = profit.index(min(profit))

    # Prints the final analysis
    print("Financial Analysis")
    print("----------------------------")
    print(f"Total Months: {len(date)}")
    print(f"Total: ${sum(profit)}")
    print(f"Average Change: ${round(statistics.mean(change),2)}")
    print(f"Greatest Increase in Profits: {date[max_index]} ${max(profit)}")
    print(f"Greatest Decrease in Profits: {date[min_index]} ${min(profit)}")

# Writes the final analysis to a text file
with open(output_path,'w') as writer:
    writer.write("Financial Analysis\n")
    writer.write("----------------------------\n")
    writer.write(f"Total Months: {len(date)}\n")
    writer.write(f"Total: ${sum(profit)}\n")
    writer.write(f"Average Change: ${round(statistics.mean(change),2)}\n")
    writer.write(f"Greatest Increase in Profits: {date[max_index]} ${max(profit)}\n")
    writer.write(f"Greatest Decrease in Profits: {date[min_index]} ${min(profit)}\n")
