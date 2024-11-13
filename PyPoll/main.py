# -*- coding: UTF-8 -*-
"""PyPoll Homework Starter File."""

# Import necessary modules
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "election_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "election_analysis.txt")  # Output file path

# Initialize variables to track the election data
total_votes = 0  # Track the total number of votes cast
 
# Define lists and dictionaries to track candidate names and vote counts
candidate_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0

# Open the CSV file and process it
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Skip the header row
    header = next(reader)

    # Loop through each row of the dataset and process it
    for row in reader:
        # Print a loading indicator (for large datasets)
        print(". ", end="")
        
        # Increment the total vote count for each row
        total_votes += 1

        # Get the candidate's name from the row
        candidate = row[2].strip()  # Use strip() to remove any leading/trailing spaces

        # If the candidate is not already in the candidate list, add them
        if candidate not in candidate_votes:
            candidate_votes[candidate] = 0

        # Add a vote to the candidate's count
        candidate_votes[candidate] += 1

# Open a text file to save the output
with open(file_to_output, "w") as txt_file:
    # Print the header for the election results
    print("Election Results")
    txt_file.write("Election Results\n")
    print("-------------------------")
    txt_file.write("-------------------------\n")

    # Print the total vote count (to terminal)
    print(f"Total Votes: {total_votes}")
    # Write the total vote count to the text file
    txt_file.write(f"Total Votes: {total_votes}\n")

    # Loop through the candidates to determine vote percentages and identify the winner
    for candidate, votes in candidate_votes.items():
        # Calculate the percentage of votes
        vote_percentage = (votes / total_votes) * 100

        # Update the winning candidate if this one has more votes
        if votes > winning_count:
            winning_count = votes
            winning_candidate = candidate

        # Print and save each candidate's vote count and percentage
        print(f"{candidate}: {vote_percentage:.3f}% ({votes})")
        txt_file.write(f"{candidate}: {vote_percentage:.3f}% ({votes})\n")

    # Generate and print the winning candidate summary
    print("-------------------------")
    txt_file.write("-------------------------\n")
    
    # Save the winning candidate summary to the text file
    print(f"Winner: {winning_candidate}")
    txt_file.write(f"Winner: {winning_candidate}\n")
    
    # Print a separator after the winner
    print("-------------------------")