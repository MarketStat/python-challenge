# PyBank Main

import os
import csv

# Take current working directory
cwd = os.getcwd()

# Get the path
csvpath = os.path.join(cwd, "PyBank\Resources", "budget_data.csv")

month = []
profit_loss = []
rev_change = []

with open(csvpath) as csvfile:

    # Read in the CSV file
    csvreader = csv.reader(csvfile,delimiter=',')

    # Skip the header
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    # Set the columns
    for row in csvreader: 

    # Assign variables to the lists from the CSV file

        # Month is in the first column
        month.append(row[0])

        # Profit/Loss is in the second column
        profit_loss.append(int(row[1]))

    # Use a For Loop with i as an integer to go through each row to complete the revenue change calculation minus the last row
    for i in range(len(profit_loss) - 1):
        
        # Take the difference between two months and append to monthly profit change
        rev_change.append(profit_loss[i + 1] - profit_loss[i])

# Set a variable to take the average of the revenue change and round it to two decimal points
avg_rev = (round(sum(rev_change)/len(rev_change),2))

# Find the maximum value in the difference between two months and search the index to grab the next month 
great_inc_amt = max(rev_change)
great_inc_mth = rev_change.index(max(rev_change)) + 1

# Find the minimum value in the difference between two months and search the index to grab the next month 
great_dec_amt = min(rev_change)
great_dec_mth = rev_change.index(min(rev_change)) + 1

# Print out the final results

print("Financial Analysis")

print("----------------------------")

print(f"Total Months: {len(month)}")

print(f"Total: ${sum(profit_loss)}")

print(f"Average Change: {avg_rev}")

print(f"Greatest Increase in Profits: {month[great_inc_mth]} (${(str(great_inc_amt))})")

print(f"Greatest Decrease in Profits: {month[great_dec_mth]} (${(str(great_dec_amt))})")

# Path to the output file
finance_result = os.path.join(cwd, "PyBank/Analysis", "Financial_Record_Analysis.txt")

# Write the analysis to a text file
with open(finance_result, 'w') as txtfile:
    
# Write out the above analysis to a text file

    txtfile.write("Financial Analysis")

    txtfile.write("\n")

    txtfile.write("----------------------------")

    txtfile.write("\n")

    txtfile.write(f"Total Months: {len(month)}")

    txtfile.write("\n")

    txtfile.write(f"Total: ${sum(profit_loss)}")

    txtfile.write("\n")

    txtfile.write(f"Average Change: {avg_rev}")

    txtfile.write("\n")

    txtfile.write(f"Greatest Increase in Profits: {month[great_inc_mth]} (${(str(great_inc_amt))})")

    txtfile.write("\n")

    txtfile.write(f"Greatest Decrease in Profits: {month[great_dec_mth]} (${(str(great_dec_amt))})")

