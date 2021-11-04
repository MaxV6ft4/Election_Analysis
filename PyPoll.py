# Data needed to be retrieved.
#1 total number of votes cast
#2 complete list of candidates who received votes
#3 percentage of votes each candidate won
#4 total number of votes each candidate won
#5 winner of election based on popular vote

# Add our dependencies.
import csv
import os

# Assign a variable to load the file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")

# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a total vote counter.
total_votes = 0

# Declare a list of candidates.
candidate_options = []

# Declare a dictionary of votes.
candidate_votes = {}

# Declare winning candidate and winning count trackers.
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:

    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)

    # Read and print the header row.
    #headers = next(file_reader)
    #print(headers)

    # Print each row in the CSV file.
    for row in file_reader:
        
        # Add to the total vote count.
        total_votes += 1

        # Print the candidate name from each row.
        candidate_name = row[2]

        # If the candidate does not match any existing candidate,
        if candidate_name not in candidate_options:

            # Add it to the list of candidates.
            candidate_options.append(candidate_name)

            # Begin to track the candidate's vote count.
            candidate_votes[candidate_name] = 0

        # Add one vote to that candidate's count.
        candidate_votes[candidate_name] += 1

    # Determine the percentage of votes for each candidate by looping through the counts.

    # Iterate through the candidate list.
    for candidate_name in candidate_votes:

        # Gather the vote count for a candidate.
        votes = candidate_votes[candidate_name]

        # Calculate the percentage of votes.
        vote_percentage = float(votes) / float(total_votes) * 100

        # To do: print out each candidate's name, vote count and percentage of votes to the terminal.
        print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        # Determine winning vote count and candidate.

        # If the votes are greater than the winning count, 
        if (votes > winning_count) and (vote_percentage > winning_percentage):

            # Set winning_count = votes and winning_percentage = vote_percentage.
            winning_count = votes
            winning_percentage = vote_percentage

            # Set winning_candidate equal to the candidate's name.
            winning_candidate = candidate_name

    # To do: print out the winning candidate, vote count and percentage to the terminal.
        
    winning_candidate_summary = (
            f"------------------------\n"
            f"Winner: {winning_candidate}\n"
            f"Winning Vote Count: {winning_count:,}\n"
            f"Winning Percentage: {winning_percentage:.1f}%\n"
            f"------------------------\n")
    print(winning_candidate_summary)

# Print the total number of votes.
#print(total_votes)

# Print the candidate list.
#print(candidate_options)

# Print the candidate vote dictionary.
#print(candidate_votes)

# Close the file.
election_data.close()

# Using the open() function with the "w" mode we will write data to the file.
#with open(file_to_save, "w") as txt_file:

    # Write a heading 
    #txt_file.write("Counties in the Election")

    # Skip a line
    #txt_file.write("\n-------------------------")

    # Write three counties to the file.
   # txt_file.write("\nArapahoe\nDenver\nJefferson")

#Close the file
#txt_file.close()