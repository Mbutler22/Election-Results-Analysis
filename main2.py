 # Dependencies

import os
import csv

#Set path for file

csvpath =os.path.join("PyPoll", "election_data.csv")

#Set the output for the text file
text_path = 'output.text'

#Set variables
total_votes = 0
candidate_name = []
candidate_votes = {}
county_list = []
county_votes = {}
vote_counts =[]
winning_candidate =""
winning_count = 1
winning_percentage = 0
largest_county =""
largest_county_count = 0
largest_county_percentage = 0
candidate_options =[]
vote_percentage = total_votes/ 100

#Open the CSV file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header= next(csvreader)
    
    row_one = next(csvreader)

    #Get values of Row 1 and skip since there is no change
    #candidate_votes = candidate_votes + 1

    #Candidate voted for
    #candidate = line[2]

#loop process each vote
    for line in csvreader:
        total_votes = total_votes + 1
        candidate_name = line[2]
        county = line[1]
    #if candidate has other votes add to vote

        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 0
            candidate_votes[candidate_name] =1
           #candidate_index = candidate_name.index(candidate_name)
           #vote_counts[candidate_index] = vote_counts[candidate_index] + 1

        if county not in county_list:
            county_list.append(county)
            county_votes[county] = 0
            county_votes[county] + 1

    with open(text_path, "w") as txt_file:
        #Print the final vote count
        election_results =(
            f"\nElection Results\n"
            f"--------------------\n"
            f"Total Votes: {total_votes:,}\n"
            f"---------------------------\n\n"
            f"County Votes: \n")
        print(election_results, end="")
        txt_file.write(election_results)

    for county_name in county_votes:
        vote_count = county_votes[county_name]
        vote_percentage = float(vote_count) / float(total_votes) * 100
        county_results = (f"{county_name}: {vote_percentage:.1f}% ({vote_count:,})\n")
    print(county_results)
    #txt_file.write(county_results)

    if (vote_count > winning_count) and (vote_percentage > winning_percentage):
        winning_count = vote_count
        winning_county = county_name
        winning_percentage = vote_percentage


    largest_county_summary = (
        f"-------------------------\n"
        #f"Winner: {winning_county}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"--------------------------------------------\n")
    print(largest_county_summary)
    #txt.file.write(largest_county_summary)

    for candidate_name in candidate_votes:
        votes = candidate_votes.get(candidate_name)
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = ("{candidate_name}: {vote_percentage:..1f}% ({votes:,})\n")
    print(candidate_results)
    #txt_file.write(candidate_results)

    if(votes > winning_count) and (vote_percentage > winning_percentage):
        winning_counts = votes
        winning_candidate = candidate_name
        winning_percentage = vote_percentage
        print(candidate_name)
        
    winning_candidate_summary =(
        f"---------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-----------------------------\n")
    print(winning_candidate_summary)
    #txt_file.write(winning_candidate_summary)
