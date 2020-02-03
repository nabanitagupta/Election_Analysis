# The data we need to retrieve
#1. The total number of votes cast
#2. A complete list of candidates who received votes
#3. The percentage of votes each candidate won
#4. The total number of votes each candidate won
#5. The winner of the election based on popular vote. 
import csv
import os
# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources/election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")
# 1. Initialize a total vote counter.
total_votes = 0
# County List
County_list = []
# Declare the empty dictionary for storing votes for each county
County_votes = {}
# County with highest turnout and vote count tracker
County_Biggest_Turnout = ""

# Candidate Options
candidate_options = []

# Declare the empty dictionary.
candidate_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    # Read the header row.
    headers = next(file_reader)
    # Print each row in the CSV file.
    for row in file_reader:
        # Add to the total vote count.
        total_votes += 1
        # Print the county name from each row.
        county_name = row[1]
        # If the county does not match any existing counties...
        if county_name not in County_list:
            # Add it to the list of counties
            county_List.append(county_name)
            # Begin tracking each county's vote count. 
            County_votes[county_name] = 0
        # Add a vote to that county's count
        County_votes[county_name] += 1
        # Determine the percentage of votes for each county by looping through the counts.
  # 1. Iterate through the county list.
    for county in county_votes:
        #Retrieve vote count of a county
        Regional_votes = county_votes[county]
        # 3. Calculate the percentage of votes.
        vote_percentage = float(Regional_votes) / float(total_votes) * 100
        #  To do: print out each county's name, vote count, and percentage of
        # votes to the terminal.
        #print(f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n")
        county_results = (f"{county}: {vote_percentage:.1f}% ({Regional_votes:,})\n")
        # Print each county, relevent voter count, and percentage to the terminal.
        print(county_results)
        # Save the county results to the text file
        txt_file.write(county_results)
        # Determine largest county turnout
        # Determine if the votes is greater than the winning count.
        if (Regional_votes > highest_count) and (vote_percentage > highest_percentage):
            # If true then set highest_count = votes and highest_percent =
            # vote_percentage.
            highest_count = Regional_votes
            highest_percentage = vote_percentage
            # And, set the highest turnout county equal to the caounty's name.
            County_Biggest_Turnout = county
    # Print out the winning candidate, vote count and percentage to terminal
            Largest_Turnout_County = (
            f"-------------------------\n"
            f"Largest County Turnout: {County_Biggest_Turnout}\n"
            f"-------------------------\n")
    print(Largest_Turnout_County)
    # Save the county result to the text file.
    txt_file.write(Largest_Turnout_County)

    # Print the candidate name from each row.
    candidate_name = row[2]
    # If the candidate does not match any existing candidate...
    if candidate_name not in candidate_options:
        # Add it to the list of candidates.
        candidate_options.append(candidate_name)
        # Begin tracking that candidate's vote count. 
        candidate_votes[candidate_name] = 0
        # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

# Save the results to our text file.
with open(file_to_save, "w") as txt_file:
    
    # Print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
    # Save the final vote count to the text file.
    txt_file.write(election_results)
  # Determine the percentage of votes for each candidate by looping through the counts.
  # 1. Iterate through the candidate list.
    for candidate in candidate_votes:
      
        #Retrieve vote count of a candidate.
        votes = candidate_votes[candidate]
        # 3. Calculate the percentage of votes.
        vote_percentage = float(votes) / float(total_votes) * 100
        #  To do: print out each candidate's name, vote count, and percentage of
        # votes to the terminal.
        #print(f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n")
        candidate_results = (f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n")
      
        # Print each candidate, their voter count, and percentage to the terminal.
        print(candidate_results)
        # Save the candidate results to our text file.
        txt_file.write(candidate_results)
        # Determine winning vote count and candidate
        # Determine if the votes is greater than the winning count.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            # If true then set winning_count = votes and winning_percent =
            # vote_percentage.
            winning_count = votes
            winning_percentage = vote_percentage
            # And, set the winning_candidate equal to the candidate's name.
            winning_candidate = candidate
    # Print out the winning candidate, vote count and percentage to
    #   terminal.
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)
    # Save the winning candidate's results to the text file.
    txt_file.write(winning_candidate_summary)
