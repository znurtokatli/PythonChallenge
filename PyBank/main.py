import os
import csv

# define variables
months = []
value_changes = [] 
count_months = 0
net_value = 0
previous_month_value = 0
value_change = 0

# change directory to the current file path and get source file path
os.chdir(os.path.dirname(__file__))
source_file_path = os.path.join("Resources", "budget_data.csv" )

# open source file 
with open(source_file_path, newline="") as csvfile:

    #file reader
    csv_reader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)

    # read rows 
    for row in csv_reader:

        count_months += 1

        current_month_value = int(row[1])
        net_value += current_month_value

        if (count_months == 1): #ZeroDivisionError 
            previous_month_value = current_month_value
            continue
        else: 
            value_change = current_month_value - previous_month_value
            months.append(row[0]) 
            value_changes.append(value_change)
            previous_month_value = current_month_value

        # sum and average of profit/loss value from array over the entire period
        sum_value = sum(value_changes)
        mean_value = round(sum_value/(count_months - 1), 2)

        # greatest increase&decrease in profits over the entire period
        highest_change = max(value_changes)
        lowest_change = min(value_changes)

        highest_month_index = value_changes.index(highest_change)
        lowest_month_index = value_changes.index(lowest_change)

        highest_month = months[highest_month_index]
        lowest_month = months[lowest_month_index]

# export a text file with the results
output_file = os.path.join("Analysis", "Analysis.txt")
with open(output_file, "w") as outfile:

    outfile.write("Financial Analysis\n")
    outfile.write("------------------\n")
    outfile.write(f"Total Months: {count_months}\n")
    outfile.write(f"Total: ${net_value}\n")
    outfile.write(f"Average Change: ${mean_value}\n")
    outfile.write(f"Greatest Increase in Profits: {highest_month} (${highest_change})\n")
    outfile.write(f"Greatest Decrease in Losses: {lowest_month} (${lowest_change})\n")


# print the analysis to the terminal
print("Financial Analysis")
print("------------------")
print(f"Total Months: {count_months}")
print(f"Total: ${net_value}")
print(f"Average Change: ${mean_value}")
print(f"Greatest Increase in Profits: {highest_month} (${highest_change})")
print(f"Greatest Decrease in Losses: {lowest_month} (${lowest_change})")




