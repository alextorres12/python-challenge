import os
import csv

# Set CSV path for reading
csvpath = os.path.join('Resources','election_data.csv')

# Set path to output .txt file
output_path = os.path.join('Analysis','election_results.txt')

# Initialize list to store candidate information
votes = []
count_by_candidates = {}


# Read CSV
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    # Skip header
    next(csvreader)

    # Adds all votes to a list
    for row in csvreader:
        votes.append(row[2])

    # Adds all unique candidates to a list
    for each in votes:
        if each not in count_by_candidates:
            count_by_candidates.update({each:0})

    for each in votes:
        count_by_candidates[each] = count_by_candidates[each]+1
    

    
    print(f"Total Votes: {len(votes)}")
    print(count_by_candidates)


    
    

