# This Script reads a CSV resourse file for PYPoll project.
# The Poll dataset is called election_data.csv
# The dataset is composed of three columns:  "Ballot ID", "County", and "Candidate"

# Task: Python script that analyzes the votes and calculate each of the following values:
#	The total number of votes cast
#	A complete list of candidates who recieved votes
#	The percentage of votes each candidate won
#	The total number of votes each candidate won
#	The winner of the election based on popular vote

# Utilize Built-in Modules for Python to navigate across our file system:
#	Import os - lets Python know our operating system is Windows

#	Import csv - module for importing csv files

# back up one directory and then forward one directory to read csv file

#The final script should both print the analysis to the terminal (script file) and export a text file in the same directory.
#	Script file is located in analysis folder
#	Dataset file is located in Resources folder

import os
import csv
from collections import Counter

# Navigate to the correct directory
current_directory = os.getcwd()
csv_file_path = os.path.join(current_directory, '..', 'resources', 'election_data.csv')

# Initialize variables
total_votes = 0
candidate_votes = Counter()

# Read the CSV file
with open(csv_file_path, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    next(csvreader)  # Skip the header

    # Process each vote
    for row in csvreader:
        total_votes += 1
        candidate_votes[row[2]] += 1

# Prepare the election results
results = ["Election Results\n-------------------------"]
results.append(f"Total Votes: {total_votes}\n-------------------------")

# Calculate and append votes for each candidate
for candidate, votes in candidate_votes.items():
    percentage = (votes / total_votes) * 100
    results.append(f"{candidate}: {percentage:.3f}% ({votes})")

results.append("-------------------------")

# Determine and append the winner
winner = max(candidate_votes, key=candidate_votes.get)
results.append(f"Winner: {winner}\n-------------------------")

# Print and write the results to a file
output_file_path = os.path.join(current_directory, 'Poll_Results.txt')
with open(output_file_path, 'w') as textfile:
    for line in results:
        print(line)
        textfile.write(line + "\n")
