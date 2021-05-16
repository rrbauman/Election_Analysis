# The data we need to retrieve.
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes.
# 3. The percentage of votes each candidate won.
# 4. The total number of votes each candidate won.
# 5. The winner of the election based on popular vote.
# Assign a variable for the file to load and the path.
##file_to_load = 'resources/election_results.csv'

#Open the election results and read the file.
##with open(file_to_load) as election_data: 

# To do: perform analysis.
##    print(election_data)
# Add our dependencies
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("resources", "election_results.csv")
# Create a filename variable to a direct or indirect path to the file. 
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Using the open() function and with the "w" mode we will write data to the file.
with open(file_to_load) as election_data:
    # To do: read and analyze the data here.
    file_reader = csv.reader(election_data)

    # Print each row in the CSV file.
    #for row in file_reader:
    #    print(row)
    headers = next(file_reader)

    #Print each row in the CSV file.
    for row in file_reader:
        print(row)