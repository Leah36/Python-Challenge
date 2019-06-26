
#Import modules os and csv.
import os
import csv 

#Create CSV file

election_data_csv_path = os.path.join("C:/Users/Leah/Desktop/python-challenge/PyPoll/Resources/Copy of election_data.csv")
#The list to capture the names of candidates
candidates = []

#The list to capture the number of votes each candidates gather
percent_votes = []

#The counter for the total number of votes
total_votes = 0

with open(election_data_csv_path, newline = "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    csv_header = next(csvreader)

for row in csvreader:

    #Add to our vote-countr
    total_votes = 1    

#If the candidate is not on our list, add his/her name to our list, along with 
#a vote in his/her name.
#If he/she is already on our list, we will simply add a vote in his/her name.

if row[2] not in candidates:
        candidates.append(row[2])
        index = candidates.index(row[2])
        num_votes.append(1)

else:
        index = candidates.index(row[2])
        num_votes[index] += 1
 
    # Add to percent_votes list 
for votes in num_votes:
        percentage = (votes/total_votes) * 100
        percentage = round(percentage)
        percentage = "%.3f%%" % percentage
        percent_votes.append(percentage)


    # Find the winning candidate

winner = max(num_votes)
index = num_votes.index(winner)
winning_candidate = candidates[index]

# Displaying results
print("Election Results")
print("--------------------------")
print(f"Total Votes: {str(total_votes)}")
print("--------------------------")
for i in range(len(candidates)):
    print(f"{candidates[i]}: {str(percent_votes[i])} ({str(num_votes[i])})")
print("--------------------------")
print(f"Winner: {winning_candidate}")
print("--------------------------")

# Exporting to .txt file
output = open("output.txt", "w")
line1 = "Election Results"
line2 = "--------------------------"
line3 = str(f"Total Votes: {str(total_votes)}")
line4 = str("--------------------------")
output.write('{}\n{}\n{}\n{}\n'.format(line1, line2, line3, line4))
for i in range(len(candidates)):
    line = str(f"{candidates[i]}: {str(percent_votes[i])} ({str(num_votes[i])})")
    output.write('{}\n'.format(line))
line5 = "--------------------------"
line6 = str(f"Winner: {winning_candidate}")
line7 = "--------------------------"
output.write('{}\n{}\n{}\n'.format(line5, line6, line7))