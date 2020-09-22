import os
import csv

# Set CSV path for reading
csvpath = os.path.join('Resources','election_data.csv')

# Set path to output .txt file
output_path = os.path.join('Analysis','election_results.txt')

# Initialize dictionary to store candidate information and vote counts
count_by_candidates = {}


# Read CSV
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    # Skip header
    next(csvreader)

    # Iterates through all rows of the csv
    for row in csvreader:
        # Adds unique candidates as keys to dictionary
        if row[2] not in count_by_candidates:
            count_by_candidates.update({row[2]:0})
        # Adds vote totals to each candidate
        else:
            count_by_candidates[row[2]] = count_by_candidates[row[2]]+1

    # Determine the total votes and election winner
    total = sum(count_by_candidates.values())
    winner = max(count_by_candidates, key=count_by_candidates.get)

    print("Election Results")
    print("-------------------------")
    print(f"Total Votes: {total}")
    print("-------------------------")

    # Iterates through the dictionary to print each Candidate and their respective vote totals/percentages
    for each in count_by_candidates:
        print(f"{each}: {round(count_by_candidates[each]/total*100,3)}% ({count_by_candidates[each]})")
    print("-------------------------")
    print(f"Winner: {winner}")
    print("-------------------------")

# Write the same printed information to a .txt file
with open(output_path, 'w') as writer:
    writer.write("Election Results\n")
    writer.write("-------------------------\n")
    writer.write(f"Total Votes: {total}\n")
    writer.write("-------------------------\n")
    for each in count_by_candidates:
        writer.write(f"{each}: {round(count_by_candidates[each]/total*100,3)}% ({count_by_candidates[each]})\n")
    writer.write("-------------------------\n")
    writer.write(f"Winner: {winner}\n")
    writer.write("-------------------------\n")




    
    

