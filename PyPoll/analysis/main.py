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

# Set the path for the election_data.csv file
current_directory = os.getcwd()
csv_file_path = os.path.join(current_directory, '..', 'resources', 'election_data.csv')

# Initialize variables
total_votes = 0
candidate_votes = Counter()

# Read the CSV file
with open(csv_file_path, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    header = next(csvreader)  # Skip the header row

    # Process each vote
    for row in csvreader:
        total_votes += 1
        candidate_votes[row[2]] += 1

# Print the election results
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")

# Calculate and print votes for each candidate
for candidate, votes in candidate_votes.items():
    percentage = (votes / total_votes) * 100
    print(f"{candidate}: {percentage:.3f}% ({votes})")

print("-------------------------")

# Determine the winner
winner = max(candidate_votes, key=candidate_votes.get)
print(f"Winner: {winner}")
print("-------------------------")

