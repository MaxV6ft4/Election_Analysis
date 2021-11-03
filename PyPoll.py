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

# Open the election results and read the file.
with open(file_to_load) as election_data:

    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)

    # Read and print the header row.
    headers = next(file_reader)
    print(headers)

    # Print each row in the CSV file.
    #for row in file_reader:
        #print(row[0])

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