# Import modules
import os
import csv

# Open and read election data CSV
csvpath = os.path.join("..","PyPoll","election_data.csv")

with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)
 
    # Create variables and dictionaries
    candidate_list = {}
    row_count = 0
    vote_count = 0
    vote_percentage = 0
    winning_votes = 0
    winning_candidate = ""

    # Go through rows and count the number of votes
    for row in csvreader:
        candidate_name = row[2]
        row_count = row_count + 1
        if candidate_name in candidate_list.keys():
            candidate_list[candidate_name] = candidate_list[candidate_name] + 1
        else:
            candidate_list[candidate_name] = 1
    
    # Print results
    print("Election Results")
    print("-------------------------------")
    print(f'Total Votes: {row_count}')
    print("-------------------------------")
    
    # Set total number of votes for each candidate
    for candidate_name in candidate_list:
        vote_count = candidate_list[candidate_name]
    
        # Get percentage of votes for each candidate
        vote_percentage = round((vote_count/row_count) * 100, 2)
        print(f'{candidate_name}: {vote_percentage}% {vote_count}')
        
        # Get winning candidate and votes
        if candidate_list[candidate_name] > winning_votes:
            winning_candidate = candidate_name
            winning_votes = candidate_list[candidate_name]
    
    # Print results
    print("-------------------------------")
    print(f'Winner: {winning_candidate}')
    print("-------------------------------")

    # Export results to text file
with open("pypoll_output.txt","w") as output_file:
    output_file.write("Election Results")
    output_file.write("\n")
    output_file.write("-------------------------------")
    output_file.write("\n")
    output_file.write(f'Total Votes: {row_count}')
    output_file.write("\n")
    output_file.write("-------------------------------")
    output_file.write("\n")
    for candidate_name in candidate_list:
        vote_count = candidate_list[candidate_name]
        vote_percentage = round((vote_count/row_count) * 100, 2)
        output_file.write(f'{candidate_name}: {vote_percentage}% {vote_count} \n')
    output_file.write("\n")
    output_file.write("-------------------------------")
    output_file.write("\n")
    output_file.write(f'Winner: {winning_candidate}')
    output_file.write("\n")
    output_file.write("-------------------------------")
    
