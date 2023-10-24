import os 
import csv

# Get the current working directory

cwd = os.getcwd()

csvpath = os.path.join(cwd, "PyPoll\Resources", "election_data.csv")

# Declare variables for the sum of votes and for the votes for each candidate

Votes_Cast = 0 
StockhamV = 0
DegetteV = 0
DoaneV = 0

with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile,delimiter=',')

    print(csvreader)

    # Print the header of the CSV file

    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    # Go through each row in 
    for row in csvreader: 

        # Loop through each of the rows and increase (+=) the value by what is in the row

        if row[2] == "Charles Casper Stockham": 
            StockhamV += 1

        elif row[2] == "Diana DeGette":
            DegetteV += 1

        elif row[2] == "Raymon Anthony Doane": 
            DoaneV += 1


        # Create a sum of the total votes by adding them up by row

        Votes_Cast += 1

 # Create two lists to take in each candidate and the total votes found in the above For Loop

cand_name = ["Charles Casper Stockham", "Diana DeGette", "Raymon Anthony Doane"]
cand_votes = [StockhamV, DegetteV, DoaneV]

# Combine the above lists in a dictionary through a zip function

cand_vote_dict = dict(zip(cand_name,cand_votes))

# Find the winner in the dictionary by using the max function

winner = max(cand_vote_dict, key=cand_vote_dict.get)

# Create variables for the percentages of votes

StockhamP = (StockhamV / Votes_Cast) * 100

DegetteP = (DegetteV / Votes_Cast) * 100

DoaneP = (DoaneV / Votes_Cast) * 100

# Print out the election results

print(f"Election Results")

print(f"----------------------------")

print(f"Total Votes: {Votes_Cast}")

print(f"----------------------------")

#change the data format of the percentages using .3f

print(f"Charles Casper Stockham: {StockhamP:.3f}% ({StockhamV})")

print(f"Diana DeGette: {DegetteP:.3f}% ({DegetteV})")

print(f"Raymon Anthony Doane: {DoaneP:.3f}% ({DoaneV})")

print(f"----------------------------")

print(f"Winner: {winner}")

print(f"----------------------------")


# Path to the output file

election_result = os.path.join(cwd, "PyPoll/Analysis", "Election_Result_Analysis.txt")

# Write the analysis to a text file

with open(election_result, 'w') as txtfile:

    txtfile.write("Election Results")

    txtfile.write("\n")

    txtfile.write("----------------------------")

    txtfile.write("\n")

    txtfile.write(f"Total Votes: {Votes_Cast}")

    txtfile.write("\n")

    txtfile.write("----------------------------")

    txtfile.write("\n")

    txtfile.write(f"Charles Casper Stockham: {StockhamP:.3f}% ({StockhamV})")

    txtfile.write("\n")

    txtfile.write(f"Diana DeGette: {DegetteP:.3f}% ({DegetteV})")

    txtfile.write("\n")

    txtfile.write(f"Raymon Anthony Doane: {DoaneP:.3f}% ({DoaneV})")

    txtfile.write("\n")

    txtfile.write("----------------------------")

    txtfile.write("\n")

    txtfile.write(f"Winner: {winner}")

    txtfile.write("\n")

    txtfile.write("----------------------------")
